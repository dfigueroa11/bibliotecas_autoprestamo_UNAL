data = machine.Pin(2,machine.Pin.IN)
clock = machine.Pin(4,machine.Pin.IN)

while True:
    values = 0
    for i in range(11):
        while clock.value():
            pass
        values |= data.value() << i
        while  not clock.value():
            pass
    values >>= 1
    print(values)