from time import sleep
from ili9341 import Display
from machine import Pin, SPI
 
spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(26), cs=Pin(15), rst=Pin(25))

display.draw_image('bibliotecash.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecash1.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecash2.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecash3.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecash4.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecash5.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecash6.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecash7.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecash8.raw', 0, 0, 240, 320)
sleep(5)

display.draw_image('bibliotecash9.raw', 0, 0, 240, 320)
sleep(5)