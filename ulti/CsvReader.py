from csv import reader

class CsvReader():
    def readCsvBy(self, path):
        print("當前路徑為：", path)
        file = open(path, newline='')
        csvReader = reader(file)
        return csvReader
