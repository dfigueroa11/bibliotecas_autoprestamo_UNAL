"""ILI9341 demo (bouncing boxes)."""
from machine import Pin, SPI
from time import sleep
from random import random, seed
from ili9341 import Display, color565
from utime import sleep_us, ticks_cpu, ticks_us, ticks_diff

#inicia exporte de general

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

#termina


class Box(object):
    def __init__(self, screen_width, screen_height, size, display, color):
        self.size = size
        self.w = screen_width
        self.h = screen_height
        self.display = display
        self.color = color
def test():
    try:
        # Baud rate of 40000000 seems about the max
        spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
        display = Display(spi, dc=Pin(26), cs=Pin(15), rst=Pin(25))
        display.clear()
        display.draw_image('bibliotecas4.raw', 0, 0, 240, 320)

        colors = [color565(255, 0, 0),
                  color565(0, 255, 0),
                  color565(0, 0, 255),
                  color565(255, 255, 0),
                  color565(0, 255, 255),
                  color565(255, 0, 255)]
        sizes = [12, 11, 10, 9, 8, 7]
        boxes = [Box(239, 319, sizes[i], display,
                 colors[i]) for i in range(6)]

        while True:
            timer = ticks_us()
            display.draw_image('bibliotecas1.raw', 0, 0, 240, 320)
            card_id_libro= perifericos.lectura(2)
            if(card_id_libro != None):
                print (card_id_libro)
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
            for b in boxes:
                
                display.draw_image('bibliotecas.raw', 0, 0, 240, 320)
                  
            # Attempt to set framerate to 30 FPS
            timer_dif = 33333 - ticks_diff(ticks_us(), timer)
            if timer_dif > 0:
                sleep_us(timer_dif)
    except KeyboardInterrupt:
        display.cleanup()
test()
