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

#COMM=Communications()

#iniciar pantalla
disp=MyDisplay(perifericos.get_spi())


#variables iniciales teclado
palabra=''
auxiliar=''
mensajeUsuario=''
aux=''
asteriscos=''
tecladoDisponible=True

#iniciar magnetizador
magnetizer = Desmagnetizer(pin1,pin2,pin3) #Configurar pines

def read_json(file_name):
    with open(file_name) as IDjson:
        data = json.load(IDjson)
    return data

def write_json(file_name,data):
    with open(file_name, 'w') as IDjson:
        json.dump(data, IDjson)


while True:

    disp.printImg('bibliotecash2.raw')
    card_id_libro= perifericos.lectura(2)
    if(card_id_libro != None):
        print (card_id_libro)
        data_libro = read_json('IDlibro.json')
        data_libro['id'] = card_id_libro  #ESTO SE ENVIARIA AL SI
            # COMM.send(topic='bibliotecas/Validate_libro', card_id_libro=card_id_libro)
               
        with open('prueba_libro.json') as prueba_libro:
            data_prueba_libro = json.load(prueba_libro)

        if(data_prueba_libro['IDlibro'] != "0"): 

            if ((data_prueba_libro['current_use'] == "True")):# En prestamo: TRUE, NO en prestamo:FALSE
                magnetizer.magnetize()
                sleep(5)
                data_prueba_libro['current_use']="False"
                write_json('prueba_libro.json',data_prueba_libro)
                #Enviar diccionario al SI- COMM.send(topic='bibliotecas/Validate_libro', )
                disp.printImg('bibliotecash4.raw')
          
                print(data_prueba_libro['current_use'])
                
            elif ((data_prueba_libro['current_use']=="False")):# En prestamo: TRUE, NO en prestamo:FALSE
                disp.printImg('bibliotecash.raw')

                card_id_persona= perifericos.lectura(1)
                if(card_id_persona != None):
                    print(card_id_persona)

                    with open('IDcarne.json') as IDcarne:
                        data_carne = json.load(IDcarne)
                        data_carne['id'] = card_id_persona  #ESTO SE ENVIARIA AL SI
                    
                    with open('prueba_persona.json') as prueba_persona:
                        data_prueba_persona = json.load(prueba_persona)
                        
                    
                    if(data_prueba_persona['user_type'] == "Estudiante"):
                        print('Funciono')
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
                            if(palabra == data_prueba_persona['clave']):
                                print('clave correcta')
                                palabra=''
                                asteriscos=''
                                clave_incorrecta = False
                                disp.printImg('bibliotecash6.raw')
                                magnetizer.demagnetize()
                                sleep(6)
                                disp.printImg('bibliotecash3.raw')
                                sleep(3)
                                disp.printImg('bibliotecash2.raw')
                                data_prueba_libro['current_use']="True"
                                write_json('prueba_libro.json',data_prueba_libro)
                                print(data_prueba_libro)
                                #Enviar diccionario actualizado a la SI, Id libro y id user para vincular
                            elif (palabra != data_prueba_persona['clave']):
                                disp.printImg('bibliotecash5.raw')
                                palabra=''
                                asteriscos=''
                                print('Clave incorrecta')
                    else:
                        print('No es estudiante')                    
                else:
                    print('No ha sido leido el carne')
            else:
                print('El estado del libro no es claro')
        else:
            print('No se ha asignado el ID del libro al json del libro') 
   
    else:
        print('No ha sido leido el libro')
    sleep(1)   
        

 



