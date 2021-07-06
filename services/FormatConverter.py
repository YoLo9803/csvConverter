from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.styles import Alignment
from openpyxl.styles import numbers

class FormatConverter():
    def __init__(self):
        self.__data = None
        self.__columnMap = {1: 0, 2: 2, 3: 9, 4: 15, 5: 18, 6: 20, 7: 22, 8: 25}

    def process(self, workbook):
        result = Workbook()
        ws = result.active
        sheets = workbook.sheets()
        self.__addTimeStampToLastColumn(sheets[0])
        return result

    def __addTimeStampToLastColumn(self, table):
        print(table.col_values(0))
