import RPi.GPIO as GPIO
from time import sleep

#ssh <usuario>@<IP de la Raspberry Pi>
#ssh pi@10.101.2.250
#user: pi
#IP fija: 10.101.2.250
#pass: DAM2
#sudo apt-get update
#sudo apt-get -y install python3-rpi.gpio


#Pines
servoPinA = 18
servoPinB = 4
#hercios = 50
#angulo = 90

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPinA, GPIO.OUT)
GPIO.setup(servoPinB, GPIO.OUT)


def abrirServoA (servoPinA,hercios):
    a = GPIO.PWM(servoPinA, hercios)
    a.start(0)
    try:
         a.ChangeDutyCycle(5)
         sleep(0.5)
         a.ChangeDutyCycle(30)
         sleep(0.5)
         a.ChangeDutyCycle(60)
         sleep(0.5)
         a.ChangeDutyCycle(90)
         sleep(0.5)
    except KeyboardInterrupt:
        a.stop()
        GPIO.cleanup()


def abrirServoB (servoPinB,hercios):
    a = GPIO.PWM(servoPinB, hercios)
    a.start(0)
    try:
         a.ChangeDutyCycle(5)
         sleep(0.5)
         a.ChangeDutyCycle(30)
         sleep(0.5)
         a.ChangeDutyCycle(60)
         sleep(0.5)
         a.ChangeDutyCycle(90)
         sleep(0.5)
    except KeyboardInterrupt:
        a.stop()
        GPIO.cleanup()




def cerrarServoA (servoPinA,hercios):
    a = GPIO.PWM(servoPinA, hercios)
    a.start(90)
    try:
         a.ChangeDutyCycle(85)
         sleep(0.5)
         a.ChangeDutyCycle(60)
         sleep(0.5)
         a.ChangeDutyCycle(30)
         sleep(0.5)
         a.ChangeDutyCycle(0)
         sleep(0.5)
    except KeyboardInterrupt:
        a.stop()
        GPIO.cleanup()




def cerrarServoB (servoPinB,hercios):
    a = GPIO.PWM(servoPinB, hercios)
    a.start(90)
    try:
         a.ChangeDutyCycle(85)
         sleep(0.5)
         a.ChangeDutyCycle(60)
         sleep(0.5)
         a.ChangeDutyCycle(30)
         sleep(0.5)
         a.ChangeDutyCycle(0)
         sleep(0.5)
    except KeyboardInterrupt:
        a.stop()
        GPIO.cleanup()


