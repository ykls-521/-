import xlrd
from xlutils.copy import copy  #


# 1- 读取excel数据  [(),(),()]
def get_excelData(sheetName, startRow, endRow, body=6, repsData=8):
    resList = []
    excelDir = '../data/测试用例-v1.4.xls'
    workBook = xlrd.open_workbook(excelDir)  # 打开excel文件
    # sheets = workBook.sheet_names()
    # 2- 取对应的sheet来操作
    workSheet = workBook.sheet_by_name(sheetName)
    # 获取单元格
    # print(workSheet.cell(1,6).value)#请求的body
    # print(workSheet.cell(1, 8).value)  # 请求的body
    # print(workSheet.nrows)

    for one in range(startRow - 1, endRow):  # [(),(),()]
        resList.append((workSheet.cell(one, body).value, workSheet.cell(one, repsData).value))
    return resList


# print(get_excelData('1-登录接口',2,5))
# for one in get_excelData('1-登录接口',2,5):
#     print(one)

# 2- 写入数据
def set_excelData(sheetIndex, startRow, endRow, colNum, inData, excelOutDir='../report/res.xls'):  # inData---列表
    excelDir = '../data/测试用例-v1.4.xls'
    workBook = xlrd.open_workbook(excelDir, formatting_info=True)  # 打开excel文件
    newWorkBook = copy(workBook)
    newWorkSheet = newWorkBook.get_sheet(sheetIndex)
    idx = 0
    for one in range(startRow - 1, endRow):
        newWorkSheet.write(one, colNum, inData[idx])  # write(行，列，内容)
        idx += 1
    newWorkBook.save(excelOutDir)


set_excelData('1-登录接口', 2, 5, 9, ['1', '2', '3', '4'])
