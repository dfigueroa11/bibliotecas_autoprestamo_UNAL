from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from machine import SoftSPI
import math
import time


#spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
#display = Display(spi, dc=Pin(26), cs=Pin(15), rst=Pin(25))
#broadway = XglcdFont('fonts/EspressoDolce18x24.c', 18, 24)

class MyDisplay:
    def __init__(self, spi):
        self.dc=26
        self.cs=15
        self.rst=25
        self.spi=spi
        self.display=Display(self.spi, dc=Pin(self.dc), cs=Pin(self.cs), rst=Pin(self.rst))
        self.font = XglcdFont('EspressoDolce18x24.c', 18, 24)
        # Chévere unispace, espresso, arcade
        self.message='Bienvenido'
    def spiInit(self, spi, dc=26, cs=15, rst=25, baudrate=1000000000):
        self.dc=dc
        self.cs=cs
        self.rst=rst
        self.baudrate=baudrate
        self.spi = spi
        self.display = Display(spi, dc=Pin(dc), cs=Pin(cs), rst=Pin(rst))
        self.font = XglcdFont('EspressoDolce18x24.c', 18, 24)
    def printShortText(self, text):
        print('Debe imprimir texto corto')
        self.display.draw_text(100, 100, text, self.font, color565(255, 255, 255), color565(204, 53, 94))# x, y, texto, fuente, color de letra, color de fondo de letra
    def printText(self, text, vspace=0, hspace=0):
        print('Debe imprimir texto')
        
        # Font depending parameters
        lineCharacters=20-hspace; # Set 23 for Broadway
        ypoints=20 # 14 for Broadway
        xpoints=11 # 9 for Broadway
        #
        
        ceiling=math.ceil(len(text)/lineCharacters)
        counter=0
        if ceiling>1:
            aux_matrix=['']*ceiling
            while len(text)>lineCharacters:
                aux_matrix[counter]=text[0:lineCharacters]
                text=text[lineCharacters:len(text)]
                counter+=1
            if len(text)>0:
                aux_matrix[counter]=text[0:len(text)]
                counter+=1
                
            for x in range(counter):
                spaces=lineCharacters-len(aux_matrix[x])
               # print(aux_matrix[x][1])
                spaces=math.floor(spaces/2)
                char=' '
                if x>0:
                    if x<counter-1:
                        if(aux_matrix[x+1][0]!=' ')&(aux_matrix[x][len(aux_matrix[x])-1]!=' '):
                            char='-'
                else:
                    if aux_matrix[x+1][1]!=' ':
                        char='-'
                #clearing=' '*len(aux_matrix[x]+char)
                #self.display.draw_text((hspace+spaces)*xpoints, (vspace+x)*ypoints, clearing, self.font, color565(0, 0, 0), color565(255, 255, 255))
                self.display.draw_text((hspace+spaces)*xpoints, (vspace+x)*ypoints, aux_matrix[x]+char, self.font, color565(0, 0, 0), color565(255, 255, 255))

        else:
            self.display.draw_text((hspace)*xpoints, (vspace)*ypoints, text, self.font, color565(0, 0, 0), color565(255, 255, 255))

      #  self.display.cleanup()
       # self.display.reset_mpy()
       
    def printImg(self,nombre):
        print('Imprime Imagen')
        self.display.draw_image(nombre, 0, 0, 240, 320)
        
        