import perifericos
import json
import machine

from machine import SoftSPI
import math
#importar para pantalla
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from displayLib import MyDisplay

import teclado 
from Desmagnetizador import Desmagnetizador 

COMM=Communications()

#iniciar pantalla
disp=MyDisplay(perifericos.get_spi())

#iniciar magnetizador
magnetizer = Desmagnetizador(16,21,17) #16 fan, 21 pwm 2, 17 pwm 1

def read_json(file_name):
    with open(file_name) as IDjson:
        data = json.load(IDjson)
    return data

def write_json(file_name,data):
    with open(file_name, 'w') as IDjson:
        json.dump(data, IDjson)

def read_book_id():
    card_id_book = perifericos.lectura(2)
    while card_id_book == None :
       card_id_book = perifericos.lectura(2)
       sleep(0.5)
       print (card_id_book)
    return card_id_book

def ask_SI_for_book_info(card_id_book):
    #dic_id_book={
    #"id" : card_id_book
    #}
    #write_json('ID_book.json',dic_id_book)
    COMM.send(topic='Bibliotecas/Validate_book', ID_book=card_id_book)
    #client.publish(b'SI/Validate_book',ID_book.json,True,1)

def receive():#Revisar
        topic, message = getValues()
        if pending_incoming_message==False and  pending_incoming_message!=last_pending:
            last_topic=str(topic,'utf-8')
            last_message=message
        if (str(topic,'utf-8')!= last_topic) or (message!=last_message):
            pending_incoming_message=True
        last_pending=pending_incoming_message
        return topic, message, pending_incoming_message

def receive_MQTT():#Revisar
    topic, message, pending_incoming_message=receive()
    if pending_incoming_message==True:
        if str(topic,'utf-8')=='Bibliotecas/Validate_user':
            message_user=message
            data_json=read_json(message_user)
        elif str(topic,'utf-8')=='Bibliotecas/Validate_book':
            message_book=message
            data_json=read_json(message_book)
            
        pending_incoming_message==False
    
    return data_json

def invalid_book(book_json):
    return book_json['IDlibro'] == '0'

def show_invalid_book():
    disp.printImg('bibliotecash11.raw')

def is_borrowed(book_json):
    return book_json['current_use'] == 'True'#Esta en prestamo

def update_book_status_borrowed(book_json):#Pasa a no estar en prestamos
    book_json['current_use'] = 'False'
    return book_json

def update_book_status_no_borrowed(book_json):#Pasa a estar en prestamo
    book_json['current_use'] = 'True'
    return book_json

def send_book_info_SIGiveback(book_json_updated):
    #write_json('book.json',book_json_updated)
    #client.publish(b'SI/Give_back',book.json,True,1)
    COMM.send(topic='Bibliotecas/Give_back', book_json_updated=book_json_updated)

def send_info_SIBorrow(book_json_updated):
    #write_json('loan.json',book_json_updated,user_json)
    #client.publish(b'SI/Borrow',loan.json,True,1)
    COMM.send(topic='Bibliotecas/Borrow', book_json_updated=book_json_updated)

def no_borrowed(book_json):
    return book_json['current_use'] == 'False'#No esta en prestamo

def read_user_id():
    card_id_user = perifericos.lectura(1)
    while card_id_user == None :
       card_id_user = perifericos.lectura(1)
       sleep(0.5)
       print (card_id_user)
    return card_id_user

def ask_SI_for_user_info(card_id_user):
    #dic_id_user={
    #"id" : card_id_user
    #}
    #write_json('ID_user.json',dic_id_user)
    COMM.send(topic='Bibliotecas/Validate_user', ID_user=card_id_user)
    #client.publish(b'SI/Validate_user',ID_user.json,True,1)

def validate_user(user_json):
    return user_json['user_type'] == 'Estudiante'

def book_borrowing(user_json, book_json):
    print('Funciono')
    palabra=''
    auxiliar=''
    mensajeUsuario=''
    aux=''
    asteriscos=''

    clave_incorrecta = True
    while  clave_incorrecta:
        tecladoDisponible=True
        disp.printImg('bibliotecash1.raw')
        while tecladoDisponible:                                
            auxiliar=teclado.readLetter()
            if auxiliar==-1:
                pass
            elif auxiliar!='enter'and auxiliar!='delete':
                palabra=palabra+auxiliar
                asteriscos=asteriscos+'* '
                print(palabra)
            elif auxiliar=='delete':
                print('borra palabra')
                aux = palabra[:-1]
                asteriscos=asteriscos[:-2]
                palabra=aux
                disp.printShortText('             ')
                print(palabra)
            elif  auxiliar=='enter':
                tecladoDisponible=False
            disp.printShortText(asteriscos)
        if(palabra == user_json['clave']):
            print('clave correcta')
            palabra=''
            asteriscos=''
            clave_incorrecta = False
            disp.printImg('bibliotecash6.raw')
            magnetizer.demagnetize()
            
            disp.printImg('bibliotecash3.raw')
            sleep(3)
            disp.printImg('bibliotecash2.raw')
            book_json_updated = update_book_status_no_borrowed(book_json)
            #write_json('book.json',book_json_updated) 
            send_info_SIBorrow(book_json_updated)
            print(book_json_updated)
            
        elif (palabra != user_json['clave']):
            disp.printImg('bibliotecash5.raw')
            palabra=''
            asteriscos=''
            print('Clave incorrecta')

while True:
    COMM.check_message()
    disp.printImg('bibliotecash2.raw')
    card_id_book = read_book_id()
    ask_SI_for_book_info(card_id_book)
    book_json = receive_MQTT()
    #book_json=read_json('book.json')

    if (invalid_book(book_json)):
        show_invalid_book()
        pass

    if is_borrowed(book_json):
        magnetizer.magnetize()
        sleep(5)
        book_json_updated = update_book_status_borrowed(book_json)
        send_book_info_SIGiveback(book_json_updated)
        #write_json('book.json',book_json_updated) 
        disp.printImg('bibliotecash4.raw')
        print(book_json_updated['current_use'])

    elif no_borrowed(book_json):
        disp.printImg('bibliotecash.raw')
        card_id_user =  read_user_id()
        ask_SI_for_person_info(car_id_user)
        user_json = receive_MQTT()
        #user_json=read_json('user.json') 
        if (validate_user(user_json)):
            book_borrowing(user_json,book_json)
