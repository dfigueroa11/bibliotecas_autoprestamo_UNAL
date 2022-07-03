import perifericos
import json
import machine
from clases_objetos import Libro, Persona
from ili9341 import Display, color565
from machine import Pin, SPI, PWM
from xglcd_font import XglcdFont
from machine import SoftSPI
import math
from time import sleep


#Biblioteca = 'CyT' 

#disp=MyDisplay(perifericos.get_spi())

Persona_1 = Persona()
#Persona_2 = Persona()

Libro_1 = Libro()
#Libro_2 = Libro()

Libro_1.persona = Persona_1
#Libro_2.persona = Persona_2


timer_1 = machine.Timer(0)
timer_2 = machine.Timer(0)

Libro_entrega = 0
interruptCounter_1 = 0
#COMM=Communications()

spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(26), cs=Pin(15), rst=Pin(25))
broadway = XglcdFont('fonts/EspressoDolce18x24.c', 18, 24)

'''def Interrupt_T1(timer_1):
    print("interrupcion")
    global interruptCounter_1
    interruptCounter_1 = interruptCounter_1 + 1
    card_id_Bike_interr_1 = Perifericos.lectura(Libro_entrega+2)
    if(card_id_Bike_interr_1 == None):
        timer_1.deinit()
        Bike_avail[Libro_entrega].candado.estado = 'vacio'
        interruptCounter_1 = 0
        print("Se llevaron la cicla sumercé")
        with open('Prestamo_normal.json') as Prestamo_normal:
            data_send_prestamo_normal = json.load(Prestamo_normal)
            data_send_prestamo_normal['id_bike'] = Bike_avail[Libro_entrega].iD
            data_send_prestamo_normal['cedula'] = Bike_avail[Libro_entrega].persona.cedula
            #### Enviar data_send_prestamo_normal de carnet al SI, hacer un while para esperar confirmacion de receprcion
        Bike_avail[Libro_entrega].persona.reset()
        
    if(interruptCounter_1>=3):
        Perifericos.servo_close(Libro_entrega+1)
        interruptCounter_1 = 0
        with open('Devolucion_auto.json') as Devolucion:
            data_send_devolucion = json.load(Devolucion)
            data_send_devolucion['id_bike'] = Bike_avail[Libro_entrega].iD
            data_send_devolucion['danos'] = Bike_avail[Libro_entrega].danos
            data_send_devolucion['punto_de_prestamo'] = Bike_avail[Libro_entrega].candado.ubicacion
            #### Enviar data_send_devolucion de carnet al SI, hacer un while para esperar confirmacion de receprcion
        Bike_avail[Libro_entrega].persona.reset()
        timer_1.deinit()   
'''

while True:
    ##Aqui va la revision de las interrupciones por hardware
    #Poner RST
    display.draw_image('bibliotecas.raw', 0, 0, 240, 320)
    card_id_libro= perifericos.lectura(2)
    if(card_id_libro != None):
        print (card_id_libro)
        sleep(5)
        display.draw_image('bibliotecas1.raw', 0, 0, 240, 320)
        sleep(5)
        with open('IDlibro.json') as IDlibro:
            data = json.load(IDlibro)
            data['id'] = card_id_libro  #ESTO SE ENVIARIA AL SI
            '''try:
                    COMM.send(topic='bibliotecas/Validate_libro', card_id_libro=card_id_libro)
                except OSError as e:
                    print('OSError: Unable to sent ticket update. Please restart device.')
            '''
        with open('prueba_libro.json') as prueba_libro:
            data_prueba_libro = json.load(prueba_libro)
        if(data_prueba_libro['IDlibro'] != "0"): ##NO OLVIDAR: COMPARACIONES CON JSON SE HACEN EN STRING
            print (data_prueba_libro['IDlibro'])
            if ((data_prueba_libro['current_use'] == "True")):# En prestamo: TRUE, NO en prestamo:FALSE
                data_prueba_libro['current_use']="False"
                print(data_prueba_libro['current_use'])
                '''try:
                    COMM.send(topic='bibliotecas/Validate_libro', )
                except OSError as e:
                    print('OSError: Unable to sent ticket update. Please restart device.')
                '''

                
            elif ((data_prueba_libro['current_use']=="False")):
                display.draw_image('bibliotecash.raw', 0, 0, 240, 320)
                card_id_persona= perifericos.lectura(1)
                if(card_id_persona != None):
                    print(card_id_persona)
                    with open('prueba_persona.json') as prueba_persona:
                        data_prueba_persona = json.load(prueba_persona)
                        data_prueba_persona['IDcarne']=card_id_persona
                    if(data_prueba_persona['cedula'] != "0"): ##NO OLVIDAR: COMPARACIONES CON JSON SE HACEN EN STRING
                        if(data_prueba_persona['user_type'] == "Estudiante"):
                            print('Funciono')
                            break
                            #if((data_prueba_persona['restricciones'] != "True")
                        
                            #else:
                            #    disp.printShortText('Tiene deuda o sanciones. No puede hacer prestamo de libros') #Fino
           
                        else:
                            print('No es estudiante') #Fino
                    else:
                        print('error')
                else:
                    print('No ha sido leido el carne')
            else:
                print('El estado del libro no es claro')
        else:
            print('No se ha asignado el ID del libro al json del libro') #Fino
    else:
        print('No ha sido leido el libro')
         
        

 

