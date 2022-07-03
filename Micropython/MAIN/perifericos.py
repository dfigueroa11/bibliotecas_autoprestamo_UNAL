from mfrc522 import MFRC522
from machine import Pin
from machine import SPI
from machine import SoftSPI
from machine import PWM

from ili9341 import Display, color565
from xglcd_font import XglcdFont
import math
import time

sck1 = Pin(18, Pin.OUT)
mosi1 = Pin(23, Pin.OUT)
miso1 = Pin(19, Pin.OUT)
spi1 = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck1, mosi=mosi1, miso=miso1)
spi1.init()

rdr1 = MFRC522(spi=spi1, gpioRst=4, gpioCs=5)
rdr2 = MFRC522(spi=spi1, gpioRst=27, gpioCs=22)

def get_spi():
    return spi

def lectura(numero_lector):

    card_id_persona="0"
    card_id_libro="0"
    if(numero_lector==1):
        print("Por favor coloque el carn� estudiantil")
        for i in range(1,10):
            (stat, tag_type) = rdr1.request(rdr1.REQIDL)
            if stat == rdr1.OK:    
                (stat, raw_uid) = rdr1.anticoll()
                if stat == rdr1.OK:
                    card_id_persona= "C�digo carn�: 0x%02x%02x%02x%02x" % (
                        raw_uid[0],
                        raw_uid[1],
                        raw_uid[2],
                        raw_uid[3],
                    )
                    print(card_id_persona)
                    return card_id_persona
    elif(numero_lector==2):
        print("Por favor coloque libro en el espacio indicado a su izquierda")
        for i in range(1,10):
            (stat, tag_type) = rdr2.request(rdr2.REQIDL)
            if stat == rdr2.OK:    
                (stat, raw_uid) = rdr2.anticoll()
                if stat == rdr2.OK:
                    card_id_libro = "Identificaci�n libro: 0x%02x%02x%02x%02x" % (
                        raw_uid[0],
                        raw_uid[1],
                        raw_uid[2],
                        raw_uid[3],
                    )
                    print(card_id_libro)
                    return card_id_libro

    else:
        card_id_persona="0"
        print("error")
        return card_id_persona
