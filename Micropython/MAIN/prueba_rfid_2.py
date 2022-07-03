from mfrc522 import MFRC522
from machine import Pin
from machine import SoftSPI

#display
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from rfid import lectura_carne,prueba,lectura_libro




sck1 = Pin(18, Pin.OUT)
mosi1 = Pin(23, Pin.OUT)
miso1 = Pin(19, Pin.OUT)

spi1 = SoftSPI(baudrate=1000000, polarity=0, phase=0, sck=sck1, mosi=mosi1, miso=miso1)
spi1.init()
#display
spi = SPI(1, baudrate=1000000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(26), cs=Pin(15), rst=Pin(25))

rdr1 = MFRC522(spi=spi1, gpioRst=4, gpioCs=5)
rdr2 = MFRC522(spi=spi1, gpioRst=27, gpioCs=22)

display.draw_image('bibliotecas1.raw', 0, 0, 240, 320)
print("Por favor coloque el carné estudiantil")



while True:
    (stat, tag_type) = rdr1.request(rdr1.REQIDL)
   
    if stat == rdr1.OK:
        (stat, raw_uid) = rdr1.anticoll()
        if stat == rdr1.OK:
            card_id = "cóigo carné: 0x%02x%02x%02x%02x" % (
                raw_uid[0],
                raw_uid[1],
                raw_uid[2],
                raw_uid[3],
            )
            print(card_id)

    (stat2, tag_type2) = rdr2.request(rdr2.REQIDL)
    
    if stat2 == rdr2.OK:
        (stat2, raw_uid2) = rdr2.anticoll()
        if stat2 == rdr2.OK:
            card_id2 = "uid: 0x%02x%02x%02x%02x" % (
                raw_uid2[0],
                raw_uid2[1],
                raw_uid2[2],
                raw_uid2[3],
            )
            print("RFID libros: ", card_id2)

