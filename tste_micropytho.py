from machine import Pin
import time
#primeira linha 
#pinos 3, 4, 5
#p3 = Pin(3,Pin.OUT)
#p4 = Pin(4, Pin.OUT)
#p5 = Pin(5,Pin.OUT)

#segunda linha
#pinos 6,7,8

def acender_trio(x,y,z):
    grupo = x, y,z
    px = Pin(x, Pin.OUT)
    py = Pin(y,Pin.OUT)
    pz = Pin(z,Pin.OUT)
    px.value(True)
    py.value(True)
    pz.value(True)

def apagar_trio(x,y,z):
    grupo = x, y,z
    px = Pin(x, Pin.OUT)
    py = Pin(y,Pin.OUT)
    pz = Pin(z,Pin.OUT)
    px.value(False)
    py.value(False)
    pz.value(False)

while(True):
    acender_trio(3,4,5)
    acender_trio(6,7,8)
    print('ligado')
    time.sleep(1.5)
    apagar_trio(3,4,5)
    apagar_trio(6,7,8)
    print('desligado')
    time.sleep(1.5)
