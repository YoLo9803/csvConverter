from xlrd import open_workbook_xls
from csv import reader

class CsvReader():
    def __init__(self):
        self.__file = None
    
    def readCsvBy(self, path):
        print(path)
        self.__file = open(path, newline='')
        csvReader = reader(self.__file)
        return csvReader
