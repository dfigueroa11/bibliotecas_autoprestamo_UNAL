from time import sleep
from ili9341 import Display
from machine import Pin, SPI
 
spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(6), cs=Pin(15), rst=Pin(25))

display.draw_image('bibliotecas.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecas1.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecas2.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecas3.raw', 0, 0, 240, 320)
sleep(5)