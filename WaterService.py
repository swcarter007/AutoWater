import IOService
import FileService
import PlantService
import time

init = False

class WaterService:
    '''responsible for triggering the auto watering process'''
    
    def __init__(self, plantService, ioService, fileService):
        try:
            self._plantService = PlantService
            self._ioService = IOService
            self._fileService = FileService
            IOService.init()
        except Exception as e:
            raise e
        

def water(plantName):
    plant = self._plantService.getPlantFromSensor(plantName)
    consecutive_water_count = 0
    pump_pin = plant["pump_pin"]
    water_sensor_pin = plant["water_sensor_pin"]
    self._ioService.init_output(pump_pin)
    
def autoWater(plantName, delay = 5):
    plant = self._plantService.getPlantFromSensor(plantName)
    consecutive_water_count = 0
    pump_pin = plant["pump_pin"]
    water_sensor_pin = plant["water_sensor_pin"]

    self._ioService.initOutput(pump_pin)
    print("Here we go! Press CTRL+C to exit")
    try:
        while 1 and consecutive_water_count < 10:
            time.sleep(delay)
            is_wet = self._ioService.getStatus(pin = water_sensor_pin) == 0
            if not is_wet:
                if consecutive_water_count  < 5:
                    self._ioService.pumpOn(pump_pin, 1)
                    # record that plant was watered
                    self._fileService.writePlantWatered(pump_pin)

                consecutive_water_count  += 1
            else:
                consecutive_water_count  = 0

    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        self._ioService.cleanup()
   
            