#Esse código é um exemplo de loop aonde as luzes liga, desligam e respondem a input do usuário

#import GPIO
import RPi.GPIO as GPIO
import time


#definindo o pino como output
GPIO.setup(3, GPIO.OUT)

#output do pino 3  = HIGH (True) (ligado)
while(True):
    GPIO.output(3, True)
    print('ligado')
    time.sleep(.5)
    GPIO.output(3, False)
    print('desligado')
    time.sleep(.5)
    seguir = input('Repetir ? S/N')
    if seguir == 'N':
      break
