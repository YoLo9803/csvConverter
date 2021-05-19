from ulti.CsvReader import CsvReader
from services.FormatConverter import FormatConverter
from datetime import date
from csv import writer

class ConvertController():
    def __init__(self):
        self.__csvReader = CsvReader()
        self.__formatConverter = FormatConverter()

    def generateProcessedAggregateReport(self, path):
        reader = self.__obtainCsvBy(path)
        if (reader == None):
            return
        startTimeStamp = 0
        tmp = []
        for row in reader:
            if (startTimeStamp != 0 and self.__isLabelNamed('actionMenuStatus', row)):
                time = int(row[0]) - int(startTimeStamp)
                row.append(time)
                tmp.append(row)
            elif (self.__isLabelNamed('Start Load quick Link', row) and startTimeStamp == 0):
                startTimeStamp = row[0]
                print('startTimeStamp:', startTimeStamp)
        print(int(tmp[-1][-1]) + int(tmp[-1][1]))
    def __isLabelNamed(self, name, row):
        indexOfLabel = 2
        if (row[indexOfLabel] == name):
            return True
        return False

    def __searchForFirstLabelNamed(self, name, reader):
        # TODO 把index在讀檔時做成dictionary
        print(name)
        indexOfLabel = 2
        for row in reader:
            if (row[indexOfLabel] == name):
                print('row:', row)
                break  
        return row

    def __obtainCsvBy(self, path):
        reader = self.__csvReader.readCsvBy(path)
        return reader