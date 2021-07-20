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
            elif (feature == '3'):
                self.__calculateMaxAPIResponse()
            
    def __selectFeature(self):
        print("1. 計算TC-09 completion time")
        print("2. 產生Time line")
        print("3. 計算TC-09b Max API Response Time")
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
            print('測試人數：', self.__obtainCountOfTheTest(filePath), '人')
            self.__convertController.calculateCompletionTime(join(filePath, "Aggregate Report.csv"))

    def __generateTimeLineInEachReport(self):
        path = self.__requireRootFolderPath()
        if (path == 'exit'):
            return False
        dirs = listdir(path)
        for d in dirs:
            dirPath = join(path, d)
            self.__convertController.generateTimeLineForEachReportIn(dirPath)

    def __calculateMaxAPIResponse(self):
        path = self.__requireRootFolderPath()
        if (path == 'exit'):
            return False
        files = listdir(path)
        for f in files:
            filePath = join(path, f)
            print('測試人數：', self.__obtainCountOfTheTest(filePath), '人')
            itemListAPIsWithoutEmbedded = self.__convertController.calculateMaxAPIResponse(join(filePath, "Aggregate Report.csv"))
            self.__printResultOfMaxAPI(itemListAPIsWithoutEmbedded)
    
    def __printResultOfMaxAPI(self, itemListAPIsWithoutEmbedded):
        try:
            print('前五長的非collection or embedded的API為:')
            for api in itemListAPIsWithoutEmbedded[:5]:
                print('API:', api[2], ' responseTime:', api[1], ' statusCode:', api[3])
        except:
            print('計算失敗，請確認數據是否正常')

    def __obtainCountOfTheTest(self, path):
        return(path.split('-')[-1])