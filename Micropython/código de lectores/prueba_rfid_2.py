# More details can be found in TechToTinker.blogspot.com
# George Bantique | tech.to.tinker@gmail.com

from mfrc522 import MFRC522
from machine import Pin
# from machine import SPI
from machine import SoftSPI


sck1 = Pin(18, Pin.OUT)
mosi1 = Pin(23, Pin.OUT)
miso1 = Pin(19, Pin.OUT)
spi1 = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck1, mosi=mosi1, miso=miso1)
# spi2 = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck1, mosi=mosi1, miso=miso1)

# spi = SPI(2, baudrate=2500000, polarity=0, phase=0)
# Using Hardware SPI pins:
#     sck=18   # yellow
#     mosi=23  # orange
#     miso=19  # blue
#     rst=4    # white
#     cs=5     # green, DS SDA
# *************************
# To use SoftSPI,
# from machine import SOftSPI
# spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
spi1.init()
# spi2.init()

rdr1 = MFRC522(spi=spi1, gpioRst=4, gpioCs=5)
rdr2 = MFRC522(spi=spi1, gpioRst=27, gpioCs=22)
print("Por favor coloque el carné estudiantil")

# RST_Lector3=Pin 21
# CS_Lector3=Pin 14

while True:
    (stat, tag_type) = rdr1.request(rdr1.REQIDL)
    # (stat2, tag_type2) = rdr2.request(rdr2.REQIDL)

    # if stat == rdr1.OK or stat2==rdr2.OK:
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
# Write your code here :-)
