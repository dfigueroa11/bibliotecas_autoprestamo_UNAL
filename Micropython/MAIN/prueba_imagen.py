from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont

 
spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(26), cs=Pin(15), rst=Pin(25))
broadway = XglcdFont('EspressoDolce18x24.c', 18, 24)

display.draw_image('bibliotecash2.raw', 0, 0, 320, 240)
sleep(3)
display.draw_image('bibliotecash6.raw', 0, 0, 320, 240)
sleep(3)
display.draw_image('bibliotecash4.raw', 0, 0, 320, 240)
sleep(3)
display.draw_image('bibliotecash2.raw', 0, 0, 320, 240)
sleep(3)
display.draw_image('bibliotecash.raw', 0, 0, 320, 240)
sleep(3)
display.draw_image('bibliotecash1.raw', 0, 0, 320, 240)
sleep(3)
display.draw_image('bibliotecash5.raw', 0, 0, 320, 240)
sleep(3)
display.draw_image('bibliotecash1.raw', 0, 0, 320, 240)
sleep(3)
display.draw_image('bibliotecash6.raw', 0, 0, 320, 240)
sleep(3)
display.draw_image('bibliotecash3.raw', 0, 0, 320, 240)
sleep(3)
display.draw_image('bibliotecash2.raw', 0, 0, 320, 240)
sleep(3)

