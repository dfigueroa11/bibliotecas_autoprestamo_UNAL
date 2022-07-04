import perifericos
import json
import machine
<<<<<<< HEAD
=======
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
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
disp.printImg('images\bibliotecash2.raw')

#variables iniciales teclado
palabra=''
auxiliar=''
mensajeUsuario=''
tecladoDisponible=True

while True:
    
    card_id_libro= perifericos.lectura(2)
    if(card_id_libro != None):
        print (card_id_libro)
        sleep(5)
        with open('IDlibro.json') as IDlibro:
            data_libro = json.load(IDlibro)
            data_libro['id'] = card_id_libro  #ESTO SE ENVIARIA AL SI
            # COMM.send(topic='bibliotecas/Validate_libro', card_id_libro=card_id_libro)
               
        with open('prueba_libro.json') as prueba_libro:
            data_prueba_libro = json.load(prueba_libro)

        if(data_prueba_libro['IDlibro'] != "0"): 

            if ((data_prueba_libro['current_use'] == "True")):# En prestamo: TRUE, NO en prestamo:FALSE
                #Magnetizar el libro
                sleep(5)
                #data_prueba_libro['current_use']="False"
                #Enviar diccionario al SI- COMM.send(topic='bibliotecas/Validate_libro', )
                disp.printImg('images\bibliotecash4.raw')
          
                print(data_prueba_libro['current_use'])
                
            elif ((data_prueba_libro['current_use']=="False")):# En prestamo: TRUE, NO en prestamo:FALSE
                disp.printImg('images\bibliotecash.raw')
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

                        while palabra!='':
                            tecladoDisponible=True
                            while tecladoDisponible==True:
                                disp.printImg('images\bibliotecash1.raw')
                                auxiliar=teclado.readLetter()
                                if auxiliar!='enter':
                                    palabra=palabra+auxiliar
                                if auxiliar!='enter':
                                    print(palabra)
                                    disp.printText(palabra)
                                elif  auxiliar=='enter':
                                    tecladoDisponible=False  
                             pass
                             if(palabra == data_prueba_persona['clave']):
                                print('clave correcta')
                                disp.printImg('images\bibliotecash6.raw')
                                #Desmagnetizar el libro
                                sleep(6)
                                disp.printImg('images\bibliotecash3.raw')
                                #data_prueba_libro['current_use']="True"
                                #Enviar diccionario actualizado a la SI, Id libro y id user para vincular
                             elif (palabra != data_prueba_persona['clave'])
                                disp.printImg('images\bibliotecash5.raw')
                                palabra=''
                                print('Clave incorrecta')
                        pass

                         
                    else:
                        print('No es estudiante') #Fino
                    
                else:
                    print('No ha sido leido el carne')
            else:
                print('El estado del libro no es claro')
        else:
            print('No se ha asignado el ID del libro al json del libro') #Fino
   
    else:
        print('No ha sido leido el libro')
    sleep(1)   
        

 

