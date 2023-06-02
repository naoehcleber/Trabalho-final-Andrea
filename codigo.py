import RPi.GPIO as GPIO
import time 
#LEds da linha 1
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
#LEDs da linha 2
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

#LEDs da linha 3
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)



def acender_e_apagar_individual(x):
    
    GPIO.output(x,True)
    time.sleep(1.5)
    GPIO.output(x, False)
    
def acender_e_apagar_duplo(x,y):
    leds_a_acender = x,y
    GPIO.output(leds_a_acender, True)
    time.sleep(1.5)
    GPIO.output(leds_a_acender, False)
    
def acender_e_apagar_triplo(x,y,z):
    leds_a_acender = x,y,z
    GPIO.output(leds_a_acender, True)
    time.sleep(1.5)
    GPIO.output(leds_a_acender, False)
    
while (True): 
    acender_e_apagar_duplo(19,7)
    acender_e_apagar_individual(5)
    acender_e_apagar_individual(7)

