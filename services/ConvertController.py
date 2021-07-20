from ulti.CsvReader import CsvReader
from csv import writer
from os import listdir, read
from os.path import isfile, isdir, join

class ConvertController():
    def __init__(self):
        self.__csvReader = CsvReader()
        self.__ignoredAPIs = self.__parseIgnoreFile()

    def calculateCompletionTime(self, path):
        try:
            reader = self.__obtainCsvBy(path)
        except:
            print('檔案開啟失敗!')
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

    def calculateMaxAPIResponse(self, path):
        try:
            reader = self.__obtainCsvBy(path)
        except:
            print('檔案開啟失敗!')
            return None
        TimeStampOfFirstLoadQuickLinkAPI = self.__findTimeStampOfFirstLoadQuickLinkAPI(reader)
        itemListAPIs = self.__trimLoginAPIs(reader, TimeStampOfFirstLoadQuickLinkAPI)
        itemListAPIs.sort(key= lambda api: int(api[1]), reverse= True)
        itemListAPIsWithoutEmbedded = list(filter(self.__isNotComponentOrEmbedded, itemListAPIs))
        return itemListAPIsWithoutEmbedded
    
    def __parseIgnoreFile(self):
        with open('./configuration/ignoredAPIs.txt', 'r') as ignoreFile:
            return ignoreFile.read().split('\n')
    
    def __findTimeStampOfFirstLoadQuickLinkAPI(self, reader):
        for row in reader:
            if (self.__isLabelNamed('Start Load quick Link', row)):
                return row[0]
        return 0
    
    def __trimLoginAPIs(self, report, endTime):
        itemListAPIs = []
        for api in report:
            if (self.__isAPILateThan(endTime, api)):
                itemListAPIs.append(api)
        return itemListAPIs

    def __isAPILateThan(self, endTime, api):
        return api[0] >= endTime

    def __isLabelNamed(self, name, row):
        indexOfLabel = 2
        if (row[indexOfLabel] == name):
            return True
        return False

    def __isNotComponentOrEmbedded(self, api):
        return api[2] not in self.__ignoredAPIs

    def generateTimeLineForEachReportIn(self, dirPath):
        files = listdir(dirPath)
        for file in files:
            if ("With Time Line" in file):
                print("已產生過TimeLine檔")
                continue
            extension = self.__getFileExtension(file)
            if (extension == 'csv' or extension == 'jtl'):
                try:
                    reader = self.__obtainCsvBy(join(dirPath, file))
                    self.__addTimeLineToAnothorFile(self.__generateNewFileName(dirPath, file), reader)
                    print('檔案產生完成！')
                except:
                    print('轉換失敗！請檢查檔案格式與內容是否正確！')      

    def __generateNewFileName(self, path, file):
        originalFileName = file.split('.')[0]
        newFileName = originalFileName + ' With Time Line.csv'
        print('新檔案名稱為： ' + newFileName)
        return join(path, newFileName)

    def __getFileExtension(self, file):
        return file.split('.')[-1]

    def __getStartTimeStampAndWriteToFirstRow(self, firstRow, writer):
        firstRow.append(0)
        writer.writerow(firstRow)
        return firstRow[0]

    def __writeHeader(self, header, writer):
        header.append('API Start Time')
        header.append('API End Time')
        writer.writerow(header)

    def __writeRowAndAddTimeLine(self, row, startTimeStamp, writer):
        APIStartTime = int(row[0]) - int(startTimeStamp)
        row.append(APIStartTime)
        APIEndTime = APIStartTime + int(row[1])
        row.append(APIEndTime)
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
