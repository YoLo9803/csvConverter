from services.ConvertController import ConvertController
from os import listdir
from os.path import isfile, isdir, join

class UI():
    def __init__(self):
        self.__convertController = ConvertController()
    def start(self):
        while 1:
            path = self.__requireRootFolderPath()
            if (path == 'exit'):
                break
            files = listdir(path)
            for f in files:
                filePath = join(path, f)
                self.__convertController.generateProcessedAggregateReport(join(filePath, "Aggregate Report.csv"))
    def __requireFilePath(self):
        return input('請將欲轉換檔案拉入該視窗，輸入exit關閉程式：')

    def __requireRootFolderPath(self):
        return input('請將欲轉換資料夾拉入該視窗，輸入exit關閉程式：')