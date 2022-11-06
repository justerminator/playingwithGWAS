import openpyxl
from collections import defaultdict

path = "edited-BSB273CC17HSLGA15_output (1).xlsx"

# open workbook
wb_obj = openpyxl.load_workbook(path)

# get active sheet object
sheet_obj = wb_obj.active

# range of animal categories
row = 4
column = 18
burst = 180

listAnimals = []
for i in range(2, 18):
    listAnimals.append(sheet_obj.cell(row, i).value)

# sort active range
xValue = 18
colStart = 15
colEnd = 336

x = 15


dictDur = defaultdict(list)
anCounter = 0

# animal for each column
for animal in range(2, xValue):
    # initialize start time
    ptr1 = sheet_obj.cell(x, animal).value

    listDur = []
    listDur.append((sheet_obj.cell(x, 1).value, ptr1))
    while x != colEnd:
        if sheet_obj.cell(x, animal).value - ptr1 >= burst:
            ptr1 = sheet_obj.cell(x, animal).value
            listDur.append((sheet_obj.cell(x, 1).value, ptr1))
        x += 1

    dictDur[listAnimals[anCounter]] = listDur.copy()
    anCounter += 1
    x = 15



print(len(dictDur))

newSheet = openpyxl.Workbook()
sheet = newSheet.active

# create title
r = 0
for i in range(len(listAnimals)):
    r += 1
    c1 = sheet.cell(1, r + i + 1)

    c1.value = listAnimals[i]

# populate data
rowCoord = 2
colCoord = 2
for x in range(len(dictDur)):

    for y in range(len(dictDur[listAnimals[x]])):

        c2 = sheet.cell(rowCoord, colCoord)
        c2.value = dictDur[listAnimals[x]][y][0]

        c3 = sheet.cell(rowCoord, colCoord + 1)
        c3.value = dictDur[listAnimals[x]][y][1]

        rowCoord += 1


    rowCoord = 2
    colCoord += 2

newSheet.save("sample.xlsx")