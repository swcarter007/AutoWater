from Plants import plants

class PlantService:
    '''repsonsible for getting plant data based on the sensor'''

    def getPlantFromSensor(pin):
        '''gets the plant connected to the pin number'''
        for key, value in plants.items():
            if value[1]["water_sensor_pin"] is pin:
                return value            
    
        print("No plants are tied to that sensor")


    def getPlant(plant):
        '''gets the plant setup information by plant name'''
        for key, value in plants.items():
            if value[1]["name"] is plant:
                return value            
    
        print("No plants are tied to that sensor")