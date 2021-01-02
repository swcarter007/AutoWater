import unittest
from Services.FileService import FileService

class FileServiceTest(unittest.TestCase):
    def setUp(self): 
        self.fileName = "testFile.txt"
        FileService.delete(self.fileName) #delete any file written after each test
        
    def test_read_write(self):
        FileService.write(self.fileName, "test write")
        file = FileService.read(self.fileName)
        result = file == "test write"
        self.assertTrue(result)

    def test_read_no_file(self):
        file = FileService.read(self.fileName)
        result = file == ""
        self.assertTrue(result)

    def test_delete(self):
        FileService.write(self.fileName, "test delete write")
        FileService.delete(self.fileName)
        file = FileService.read(self.fileName)
        result = file == ""
        self.assertTrue(result)

    def tearDown(self):
        FileService.delete(self.fileName)

if __name__ == '__main__':
    unittest.main()