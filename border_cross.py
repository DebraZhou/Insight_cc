import csv
# Sum the total number of crossings (Value) of each type of vehicle or equipment, or passengers or pedestrians, that crossed the border that month, regardless of what port was used.
# Calculate the running monthly average of total crossings, rounded to the nearest whole number, for that combination of Border and Measure, or means of crossing.
cross_date = list()
info = list()
date_key = dict()
measure = dict()
running_monthly = dict()
filename = 'input/Border_Crossing_Entry_Data.csv'
csv_file = open(filename, encoding="utf-8")
csv_reader = csv.reader(csv_file, delimiter=',')
headers = next(csv_reader, None)
# Sum the value per border per measure per month
# row[3] = Border, row[4] = Date, row[5] = Measure, row[6] = Value
for row in csv_reader:
    current_month  = row[4]
    if current_month not in date_key:
        cross_date.append(current_month)
        date_key.update({current_month: len(cross_date)-1})
        info.append(dict())
        info[-1][row[5]] = info[-1].get(row[5],dict())
        info[-1][row[5]][row[3]] = info[-1][row[5]].get(row[3],0) + int(row[6])
    else:
        info[date_key.get(current_month)][row[5]] = info[date_key.get(current_month)].get(row[5],dict())
        info[date_key.get(current_month)][row[5]][row[3]] = info[date_key.get(current_month)][row[5]].get(row[3],0) + int(row[6])
# get the running monthly average, 282 successive month in total
cross_date.reverse()
n_month = 0
for date in cross_date:
    n_month = n_month + 1
    measure.update({date:dict()})
    running_monthly.update({date:dict()})
    for measures in info[date_key[date]].keys():
        sum_Q1 = 0
        sum_Q2 = dict()
        running_monthly[date][measures] = running_monthly[date].get(measures,dict())
        for border in info[date_key[date]][measures].keys():
            sum_Q1 = sum_Q1 + info[date_key[date]][measures][border]
            sum_Q2[border] = sum_Q2.get(border,0) + info[date_key[date]][measures][border]
            running_monthly[date][measures].update({border:round(sum_Q2[border]/n_month)})
