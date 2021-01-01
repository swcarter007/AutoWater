from plants import plants
from EmulatorGUI.GPIO import GPIO
#import RPi.GPIO as GPIO
import datetime
import time

init = False

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

def get_plant_from_sensor(pin):
    for key, value in plants.items():
        if value[1]["water_sensor_pin"] is pin:
            return value            
    
    print("No plants are tied to that sensor")


def get_plant(plant):
    for key, value in plants.items():
        if key is plant[0]:
            return value            
    
    print("No plants are tied to that sensor")


def get_last_watered(plant):
    try:
        f = open(plant[1]["name"] + "_last_watered.txt", "r")
        json = f.readLine()
        return json
    except:
        return "NEVER!"

def init_pins(plant):
    outputPin = plant["pump_pin"]
    GPIO.setup(outputPin, GPIO.OUT)
    GPIO.output(outputPin, GPIO.LOW)
    GPIO.output(outputPin, GPIO.HIGH)

    inputPin = plant["water_sensor_pin"]
    GPIO.setup(inputPin, GPIO.IN) 


def auto_water(plant, delay = 5):
    consecutive_water_count = 0
    pump_pin = plant["pump_pin"]
    water_sensor_pin = plant["water_sensor_pin"]

    print("Here we go! Press CTRL+C to exit")
   
    while 1 and consecutive_water_count < 10:
        time.sleep(delay)
        status = GPIO.input(water_sensor_pin)
        wet = status == 0
        if not wet:
            if consecutive_water_count  < 5:
                pump_on(pump_pin, 1)
                # record that plant was watered
                write_plant_watered(pump_pin)

            consecutive_water_count  += 1
        else:
            consecutive_water_count  = 0


def write_plant_watered(plantName):
    f = open(plantName + "_last_watered.txt", "w")
    f.write("Last watered {}".format(datetime.datetime.now()))
    f.close()


def pump_on(pump_pin = 7, delay = 1):
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.HIGH)


def Main():
    try:
        # loop through each plant and call auto water
        plantList = plants.items()
        for plant in plantList:
            init_pins(plant[1])

        while(True):
            for plant in plantList:
                auto_water(plant[1])

    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPI

Main()