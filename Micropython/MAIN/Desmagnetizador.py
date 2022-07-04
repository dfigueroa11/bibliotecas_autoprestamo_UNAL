
import machine
import time
import math as ma


class Desmagnetizador:

    def __init__(self,fan_pin,pwm1_pin,pwm2_pin):
        self.duty = 0.5
        self.tperiod = 20e-3
        self.fan = machine.Pin(fan_pin,machine.Pin.IN)
        self.pwm1 = machine.Pin(pwm1_pin,machine.Pin.IN)
        self.pwm2 = machine.Pin(pwm2_pin,machine.Pin.IN)
        self.fan.value(0)
        self.pwm1.value(0)
        self.pwm2.value(0)

    def turn_on_fan(self):
        self.fan.value(1)

    def turn_off_fan(self):
        self.fan.value(0)

    def drive_h_bridge(self,current_direction=0):
        if current_direction == 1:
            self.pwm1.value(0)
            self.pwm2.value(1)
            return
        if current_direction == -1:
            self.pwm1.value(1)
            self.pwm2.value(0)
            return
        self.pwm1.value(0)
        self.pwm2.value(0)
        return


    def demagnetize(self):
        for i in range(3):
            self.drive_h_bridge(1)
            time.sleep(self.tperiod*self.duty)
            self.drive_h_bridge(-1)
            time.sleep(self.tperiod*self.duty)
            n = 10
        for i in range(1,n+1):
            self.drive_h_bridge(1)
            time.sleep(self.duty*self.tperiod*(ma.exp(-(5*(i-1)/(n-1)))))
            self.drive_h_bridge(-1)
            time.sleep(self.duty*self.tperiod*(ma.exp(-(5*(i-1)/(n-1)))))
        self.drive_h_bridge(0)

    def magnetize(self):
        self.drive_h_bridge(1)
        time.sleep(self.tperiod*self.duty)
        self.drive_h_bridge(0)
