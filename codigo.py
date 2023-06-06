import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
def setup():
    # LEDs da linha 1
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    # LEDs da linha 2
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    # LEDs da linha 3
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)

def acender_individual(x):
    GPIO.output(x, True)

def apagar_individual(x):
    GPIO.output(x, False)

def acender_duplo(x, y):
    leds_a_acender = x, y
    GPIO.output(leds_a_acender, True)

def apagar_duplo(x, y):
    leds_a_acender = x, y
    GPIO.output(leds_a_acender, False)

def acender_triplo(x, y, z):
    leds_a_acender = x, y, z
    GPIO.output(leds_a_acender, True)

def apagar_triplo(x, y, z):
    leds_a_acender = x, y, z
    GPIO.output(leds_a_acender, False)

def etapa1():
    acender_individual(15)
    acender_individual(37)
    time.sleep(1.5)
    # 00X
    # 000
    # X00

def etapa2():
    acender_individual(13)
    acender_individual(23)
    acender_individual(19)
    acender_individual(29)
    time.sleep(1.5)
    # 0XX
    # X0X
    # XX0

def etapa3():
    acender_individual(11)
    acender_individual(21)
    acender_individual(31)
    time.sleep(1.5)
    # XXX
    # XXX
    # XXX

def etapa4():
    apagar_individual(15)
    apagar_individual(37)
    time.sleep(1.5)
    # XX0
    # XXX
    # 0XX

def etapa5():
    
    apagar_individual(13)
    apagar_individual(23)
    apagar_individual(19)
    apagar_individual(29)
    time.sleep(1.5)

def etapa6():
    # X00
    # 0X0
    # 00X
    apagar_individual(11)
    apagar_individual(21)
    apagar_individual(31)
    time.sleep(1.5)

def main():
    while True:
        # 000
        # 000
        # 000
        etapa1()
        etapa2()
        etapa3()
        etapa4()
        etapa5()
        etapa6()

setup()
main()
    
    
    
    