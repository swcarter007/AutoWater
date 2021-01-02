import unittest
import datetime
from Services.PlantFileService import PlantFileService
from Services.FileService import FileService

class PlantFileServiceTest(unittest.TestCase):
    def __init__(self, test):
        unittest.TestCase.__init__(self,test)
        self.plantFileService = PlantFileService(FileService, datetime)

    def setUp(self): 
        FileService.delete("testPlant_last_watered.txt") #remove existing file

    def test_getLastWatered_never(self):
        content = self.plantFileService.getLastWatered("testPlant")
        result = content == "NEVER!"
        self.assertTrue(result)

    def test_writeLastWatered(self):
        self.plantFileService.writePlantWatered("testPlant")
        content = self.plantFileService.getLastWatered("testPlant")
        result = content == "NEVER!"
        self.assertFalse(result)

    def tearDown(self):
        FileService.delete("testPlant_last_watered.txt")

if __name__ == '__main__':
    unittest.main()