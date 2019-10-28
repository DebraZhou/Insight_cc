import csv
# Sum the total number of crossings (Value) of each type of vehicle or equipment, or passengers or pedestrians, that crossed the border that month, regardless of what port was used.
# Calculate the running monthly average of total crossings, rounded to the nearest whole number, for that combination of Border and Measure, or means of crossing.
cross_date = list()
info = list()
date_key = dict()
measure = dict()
filename = 'input/Border_Crossing_Entry_Data.csv'
csv_file = open(filename, encoding="utf-8")
csv_reader = csv.reader(csv_file, delimiter=',')
headers = next(csv_reader, None)
for row in csv_reader:
    current_month  = row[4]
    if current_month not in date_key:
        cross_date.append(current_month)
        date_key.update({current_month: len(cross_date)-1})
        info.append(dict())
    info[-1][row[5]] = info[-1].get(row[5],dict())
    info[-1][row[5]][row[3]] = info[-1][row[5]].get(row[3],int(row[6])) + int(row[6])