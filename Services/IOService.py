#import RPi.GPIO as GPIO
from EmulatorGUI.GPIO import GPIO

ON = GPIO.HIGH
OFF = GPIO.LOW

class IOService:
    '''Class is responsible for communicating with the GPIO board'''
    def __init__(self, time):
        self._time = time
        GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    
    def cleanup(self):
        GPIO.cleanup() # cleanup all GPI
    
    def initOutput(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        GPIO.output(pin, GPIO.HIGH)
    
    def updatePin(self, pin, value):
        GPIO.output(pin, GPIO.LOW)
    
    def pumpOn(self, pin, delay = 1):
        self.initOutput(pin)
    
        GPIO.output(pin, GPIO.LOW)
        self._time.sleep(delay)
        GPIO.output(pin, GPIO.HIGH)
    
    #gets the current status of the pin
    def getStatus(self, pin):
        GPIO.setup(pin, GPIO.IN) 
        return GPIO.input(pin)

    