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
        #self.__copyTitleOfData(sheets[0], ws)
        #self.__copyDataInEach(sheets, ws)
        #self.__insertTitleOfSheet(ws)
        self.__addTimeStampToLastColumn(sheets[0])
        return result

    def __addTimeStampToLastColumn(self, table):
        print(table.col_values(0))

    def __copyTitleOfData(self, table, workSheet):
        for i in range(1, 9):
            col = table.col_values(self.__columnMap[i])
            for index, value in enumerate(col[:6]):
                workSheet.cell(column = i + 1, row = index + 1).value = value

    def __insertTitleOfSheet(self, workSheet):
        workSheet['D2'].value = '銳柏股份有限公司'
        workSheet['D2'].font = Font(size= 18)
        workSheet['D2'].alignment = Alignment(horizontal='center')
        workSheet.merge_cells('D2:L2')

        workSheet['F4'].value = '表別: 統計表'
        workSheet['F4'].alignment = Alignment(horizontal='center')
        workSheet.merge_cells('F4:I4')

        workSheet['F5'].value = '單況: 未結案'
        workSheet['F5'].alignment = Alignment(horizontal='center')
        workSheet.merge_cells('F5:I5')

        workSheet['A4'].value = workSheet['B4'].value
        workSheet['B4'].value = ''
        workSheet['A5'].value = workSheet['B5'].value
        workSheet['B5'].value = ''

        workSheet['J6'].value = '備註'
        workSheet['A6'].value = '項目'

    def __copyDataInEach(self, sheets, workSheet):
        indexOfFirstData = 6
        offset = 6
        for sheet in sheets:
            end = self.__getIndexOfLastData(sheet)

            for i in range(1, 9):
                col = sheet.col_values(self.__columnMap[i])
                for index, value in enumerate(col[indexOfFirstData:end]):
                    workSheet.cell(column = 1, row = index + offset + 1).value = index + offset - 5
                    workSheet.cell(column = i + 1, row = index + offset + 1).value = value
            offset += len(col[indexOfFirstData:])
    
    def __getIndexOfLastData(self, sheet):
        col = sheet.col_values(self.__columnMap[1])
        end = len(col)
        for index, value in enumerate(col):
            if "本幣總計" in value:
                end = index
        return end
