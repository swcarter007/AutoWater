class PlantFileService:
    '''Class is repsonsible for creating and reading data from a file'''

    def __init__(self, fileService, dateTime):
        try:
            self._fileService = fileService
            self._dateTime = dateTime
        except Exception as e:
            raise e
        
    def getLastWatered(self, plantName):
        '''gets the last watered response based on the plant name'''
        try:
            result = self._fileService.read(plantName + "_last_watered.txt")
            if result == "":
                return "NEVER!"
            
            return result
        except:
            return "NEVER!"

    def writePlantWatered(self, plantName):
        '''writes that the plant was watered to the output location'''
        self._fileService.write(plantName + "_last_watered.txt", "Last watered {}".format(self._dateTime.datetime.now()))
       