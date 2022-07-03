import perifericos
import json
import machine
<<<<<<< HEAD
=======
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
>>>>>>> 7ef04551e11667aed545aa45fbfc045f14c2332e
from machine import SoftSPI
import math
#importar para pantalla
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from displayLib import MyDisplay

import teclado 
#Biblioteca = 'CyT' 
<<<<<<< HEAD
=======

#disp=MyDisplay(perifericos.get_spi())

timer_1 = machine.Timer(0)
timer_2 = machine.Timer(0)

>>>>>>> 7ef04551e11667aed545aa45fbfc045f14c2332e
#COMM=Communications()

#iniciar pantalla
disp=MyDisplay(perifericos.get_spi())
disp.printImg('bibliotecas.raw')

#variables iniciales teclado
palabra=''
auxiliar=''
mensajeUsuario=''
tecladoDisponible=True

<<<<<<< HEAD
while True:
    
    card_id_libro= perifericos.lectura(2)
    if(card_id_libro != None):
        print (card_id_libro)
        sleep(5)
=======

display.draw_image('bibliotecas1.raw', 0, 0, 240, 320)
#while True:
#    pass
    
    card_id_libro= perifericos.lectura(2)
    print (card_id_libro)
>>>>>>> 7ef04551e11667aed545aa45fbfc045f14c2332e
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
<<<<<<< HEAD
            if ((data_prueba_libro['current_use'] == "True")):# En prestamo: TRUE, NO en prestamo:FALSE
                data_prueba_libro['current_use']="False"
=======

            if ((data_prueba_libro['current_use'] == "True")):# En prestamo: TRUE, NO en prestamo:FALSE
    #                 data_prueba_libro['current_use']="False"
>>>>>>> 7ef04551e11667aed545aa45fbfc045f14c2332e
                print(data_prueba_libro['current_use'])
                '''try:
                    COMM.send(topic='bibliotecas/Validate_libro', )
                except OSError as e:
                    print('OSError: Unable to sent ticket update. Please restart device.')
                '''
<<<<<<< HEAD

                
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
                            while tecladoDisponible==True:
                                auxiliar=teclado.readLetter()
                                if auxiliar!='enter':
                                    palabra=palabra+auxiliar
                                if auxiliar!='enter':
                                    print(palabra)
                                    disp.printText(palabra)
                                elif  auxiliar=='enter':
                                    tecladoDisponible=False                            
                            break
                            
=======
 
                 
            elif ((data_prueba_libro['current_use']=="False")):
                display.draw_image('bibliotecash.raw', 0, 0, 240, 320)
                card_id_persona= perifericos.lectura(1)
                if(card_id_persona != None):
                    print(card_id_persona)
                    with open('prueba_persona.json') as prueba_persona:
                        data_prueba_persona = json.load(prueba_persona)
                        data_prueba_persona['IDcarne']=car_id_persona
                    if(data_prueba_persona['cedula'] != "0"): ##NO OLVIDAR: COMPARACIONES CON JSON SE HACEN EN STRING
                        if(data_prueba_persona['user_type'] == "Estudiante"):
                            print('Funciono')
                            break
                            #if((data_prueba_persona['restricciones'] != "True")
                         
                            #else:
                            #    disp.printShortText('Tiene deuda o sanciones. No puede hacer prestamo de libros') #Fino
            
>>>>>>> 7ef04551e11667aed545aa45fbfc045f14c2332e
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
<<<<<<< HEAD
    
    else:
        print('No ha sido leido el libro')
    sleep(1)   
        

=======
          
         
 
 
>>>>>>> 7ef04551e11667aed545aa45fbfc045f14c2332e
 

