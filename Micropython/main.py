from mfrc522 import MFRC522
from machine import Pin
from machine import SoftSPI

#we need it for display
from time import sleep
from ili9341 import Display
from machine import Pin, SPI

#pin setup RFID lectors 

sck1 = Pin(18, Pin.OUT)
mosi1 = Pin(23, Pin.OUT)
miso1 = Pin(19, Pin.OUT)
spi1 = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck1, mosi=mosi1, miso=miso1)
spi1.init()

rdr1 = MFRC522(spi=spi1, gpioRst=4, gpioCs=5)
rdr2 = MFRC522(spi=spi1, gpioRst=27, gpioCs=22)
print("Por favor coloque el carné estudiantil")

#pin setup display

spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(6), cs=Pin(15), rst=Pin(25))

#initial values

borrow=false
id_student=123456789
id_book=987654


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
            
    if card_id==id_student:
        
    
