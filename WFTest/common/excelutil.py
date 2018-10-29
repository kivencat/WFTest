import xlrd


class ExcelUtil(object):
    def __init__(self, excelpath, sheetname="sheet1"):
        # 打开Excel表格
        self.data = xlrd.open_workbook(excelpath)

        # table = data.sheets()[0]             # 通过索引顺序获取
        #  table = data.sheet_by_index(0)       # 通过索引顺序获取 

        # 通过table名字定位
        self.table = self.data.sheet_by_name(sheetname)

        # 获取行列的总数
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

        # 获取第一行的关键字,list
        self.keys = self.table.row_values(0)
        print(self.keys)

    def excelresult(self):
        r =[]
        j = 1
        for i in range(self.rowNum - 1):
            s = {}
            values = self.table.row_values(j)
            for y in range(self.colNum):
                s[self.keys[y]] = values[y]
            j += 1
            print(s)
            r.append(s)
        return  r


if __name__ == "__main__":
    excelPath = r"/Users/sun/Desktop/WFTest/common/testdata.xls"  # 只能用xls，用xlxs不行
    excel = ExcelUtil(excelPath, sheetname="sheet1")
    r = excel.excelresult()
    print(r[1]["username"])

