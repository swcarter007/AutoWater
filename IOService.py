#import RPi.GPIO as GPIO
from EmulatorGUI.GPIO import GPIO

ON = GPIO.HIGH
OFF = GPIO.LOW

class IOService:
    '''Class is responsible for communicating with the GPIO board'''
        
    def init():
        GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    
    def cleanup():
        GPIO.cleanup() # cleanup all GPI
    
    def initOutput(pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        GPIO.output(pin, GPIO.HIGH)
    
    def updatePin(pin, value):
        GPIO.output(pin, GPIO.LOW)
    
    def pumpOn(pin, delay = 1):
        init_output(pin, value)
    
        GPIO.output(pin, GPIO.LOW)
        time.sleep(delay)
        GPIO.output(pin, GPIO.HIGH)
    
    #gets the current status of the pin
    def getStatus(pin):
        GPIO.setup(pin, GPIO.IN) 
        return GPIO.input(pin)

    