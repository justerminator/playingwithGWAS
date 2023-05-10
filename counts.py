import csv
from collections import defaultdict

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.cell import Cell


import pandas as pd
import ast
import openpyxl

data = pd.read_excel("Full_burst_LGA14_long.xlsx")


data_oxy = data[data["drug_group"] == 'Oxycodone']
iir_data_col = data_oxy[["inter_infusion_interval_LGA14", "rat"]]
iir_data_col = iir_data_col.dropna()


set_intervals = [(20, 39), (40, 59), (60, 79), (80, 99), (100, 119), (120, 139)]

wb = openpyxl.Workbook()
ws = wb.active
#sheet = wb['Sheet1']

# for x in range(1, len(set_intervals) + 1):
#
#     c1 = ws.cell(1, x + 1)
#     c1.value = str(set_intervals[x - 1])

rowTracker = 2

def createCounts(lst, rat):

    global rowTracker

    map_counts = defaultdict(int)

    for x in range(len(set_intervals)):
        map_counts[str(set_intervals[x])] = 0

    intermed = ast.literal_eval(lst)
    for val in intermed:
        for ind in range(len(set_intervals)):

            if set_intervals[ind][0] <= val <= set_intervals[ind][1]:

                map_counts[str(set_intervals[ind])] += 1
                print(map_counts)



    # writing to file

    for i in range(0, 6):
        c2 = ws.cell(rowTracker, 1)
        c2.value = str(rat)

        c3 = ws.cell(rowTracker, 2)
        c3.value = str(set_intervals[i])

        c4 = ws.cell(rowTracker, 3)
        c4.value = str(map_counts[str(set_intervals[i])])

        rowTracker += 1


    # for i in range(0, 6):
    #     c2 = ws.cell(rowTracker, 1)
    #     c2.value = str(rat)
    #
    #     c2 = ws.cell(rowTracker, i + 2)
    #
    #     print(rat)
    #
    #     c2.value = map_counts[str(set_intervals[i])]



    #rowTracker += 1





    return map_counts



for index, row in iir_data_col.iterrows():

    leRat = row["rat"]
    leLst = row["inter_infusion_interval_LGA14"]


    map = createCounts(leLst, leRat)


wb.save('newfile.xlsx')
