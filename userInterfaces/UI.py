from services.ConvertController import ConvertController
from os import listdir
from os.path import isfile, isdir, join

class UI():
    def __init__(self):
        self.__convertController = ConvertController()
    def start(self):
        while 1:
            feature = self.__selectFeature()
            if (feature == 'exit'):
                break
            elif (feature == '1'):
                self.__calculateCompletionTimeInAggregateReport()
            elif (feature == '2'):
                self.__generateTimeLineInEachReport()
            
    def __selectFeature(self):
        print("1. 計算TC-09 completion time")
        print("2. 產生Time line")
        return input('請選擇功能，輸入exit離開程式：')

    def __requireRootFolderPath(self):
        return input('請將欲轉換資料夾拉入該視窗，輸入exit關閉程式：')

    def __calculateCompletionTimeInAggregateReport(self):
        path = self.__requireRootFolderPath()
        if (path == 'exit'):
            return False
        files = listdir(path)
        for f in files:
            filePath = join(path, f)
            self.__convertController.calculateCompletionTime(join(filePath, "Aggregate Report.csv"))

    def __generateTimeLineInEachReport(self):
        path = self.__requireRootFolderPath()
        if (path == 'exit'):
            return False
        dirs = listdir(path)
        for d in dirs:
            dirPath = join(path, d)
            self.__convertController.generateTimeLineForEachReportIn(dirPath)