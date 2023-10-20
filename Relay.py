#This code is implemented as part of CFC 2023 for Project Nutribuddy
#The purpose of the code is to trigger the relays of nutrient tank and water tank
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.cleanup()

while (True):    
    
    
    GPIO.output(18, 1)
    print('relay1 (nutrient) turning on')
    sleep(5)
    GPIO.output(18, 0)
    print('relay1 (nutrient) turning off')
    
    GPIO.output(16, 1)
    print('relay2 (water) turning on')
    sleep(10)
    GPIO.output(16, 0)
    print('relay2 (nutrient) turning off')
    
    sleep(1)

    break

GPIO.cleanup()
