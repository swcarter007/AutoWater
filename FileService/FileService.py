import os

class FileService:
    '''FileService is responsible for reading and writing contents from a file'''

    def write(fileName, message):
        '''writes message out to file'''
        file = open(fileName, "w")
        file.write(message)
        file.close()

    def read(fileName):
        '''read the contents of a file'''
        if os.path.exists(fileName):
            file = open(fileName, "r")
            result = file.readline()
            file.close()
            return result

        return "" #returns empty string as file doesn't exist

    def delete(fileName):
        if os.path.exists(fileName):
            os.remove(fileName)
