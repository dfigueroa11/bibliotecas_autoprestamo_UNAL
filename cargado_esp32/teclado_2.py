import machine
import time

palabra=''
auxiliar=''

data = machine.Pin(32,machine.Pin.IN)
clock = machine.Pin(33,machine.Pin.IN)
keyElements = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','space','delete','enter','esc','1','2','3','4','5','6','7','8','9','0']
keyReferences = [22,30,38,37,46,54,61,62,70,69,21,29,36,45,44,53,60,67,68,77,28,27,35,43,52,51,59,66,75,26,34,33,42,50,49,58,41,102,90,118,105,114,122,107,115,116,108,117,125,112]

def kr2el(kyb):
    index = 0
    for i in keyReferences:
        if i == kyb:
            return keyElements[index]
        index = index+1
    return -1
 
def readKYBBite():
    values = 0
    for i in range(11):
        while clock.value():
            pass
        values |= data.value()<<i
        while not clock.value():
            pass
    values >>= 1
    values &= 0xff
    return values
    
def readLetter():
    kyb_aux=readKYBBite()
    while kyb_aux != 0xf0:
        kyb_aux=readKYBBite()
    kyb_aux=readKYBBite()
    element = kr2el(kyb_aux)
    return element

while True:
    auxiliar=readLetter()
    if auxiliar!='enter':
        palabra=palabra+auxiliar
    if auxiliar!='enter':
        print(palabra)
    