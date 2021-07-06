from ulti.CsvReader import CsvReader
from services.FormatConverter import FormatConverter
from datetime import date
from csv import writer
from os import listdir
from os.path import isfile, isdir, join

class ConvertController():
    def __init__(self):
        self.__csvReader = CsvReader()
        self.__formatConverter = FormatConverter()

    def calculateCompletionTime(self, path):
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

    def generateTimeLineForEachReportIn(self, dirPath):
        files = listdir(dirPath)
        for file in files:
            extension = self.__getFileExtension(file)
            if (extension == 'csv' or extension == 'jtl'):
                reader = self.__obtainCsvBy(join(dirPath, file))
                if (reader == None):
                    return
                self.__addTimeLineToAnothorFile(self.__generateNewFileName(dirPath, file), reader)
        print('檔案產生完成！')

    def __generateNewFileName(self, path, file):
        originalFileName = file.split('.')[0]
        newFileName = originalFileName + ' With Time Line.csv'
        print('newFileName: ' + newFileName)
        return join(path, newFileName)

    def __getFileExtension(self, file):
        return file.split('.')[-1]

    def __getStartTimeStampAndWriteToFirstRow(self, firstRow, writer):
        firstRow.append(0)
        writer.writerow(firstRow)
        return firstRow[0]

    def __writeHeader(self, header, writer):
        header.append('TimeLine')
        writer.writerow(header)

    def __writeRowAndAddTimeLine(self, row, startTimeStamp, writer):
        row.append(int(row[0]) - int(startTimeStamp))
        writer.writerow(row)

    def __obtainCsvBy(self, path):
        reader = self.__csvReader.readCsvBy(path)
        return reader

    def __addTimeLineToAnothorFile(self, newFileName, reader):
        with open(newFileName, 'w', newline='') as resultFile:
            csvWriter = writer(resultFile)
            self.__writeHeader(next(reader), csvWriter)
            startTimeStamp = self.__getStartTimeStampAndWriteToFirstRow(next(reader), csvWriter)
            for row in reader:
                self.__writeRowAndAddTimeLine(row, startTimeStamp, csvWriter)

