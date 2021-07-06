from csv import reader

class CsvReader():
    def readCsvBy(self, path):
        print(path)
        try:
            file = open(path, newline='')
            csvReader = reader(file)
        except:
            return None
        return csvReader
