#© Eef Lemmens

import csv
from datetime import datetime
from datetime import timedelta, date
import re

inputfile = 'Sepsis_Cases_2.csv'
output_start = 'Duration Start Sepsis Cases.csv'
start_date =  date(2013, 11, 7)
end_date = date(2015, 6, 5)

dates = []
caseID = []
dates2 = []
dates3 = []
timeseries_start_total = []
timeseries_end_total = []
timeseries_start = []
timeseries_end = []
single_dates = []
count_start = []
count_end = []

for line in open(inputfile, 'r').readlines():
    elements=line.split(';')
    row = [element.rstrip('\n') for element in elements]
    dates.append(row[2])
    caseID.append(row[0])
dates.pop(0)
caseID.pop(0)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

for single_date in daterange(start_date, end_date):
    single_dates.append(datetime.strftime(single_date,"%Y-%m-%d %H:%M:%S"))

for something in single_dates:
    timeseries_end_total.append(0)
    timeseries_end.append(0)
    timeseries_start_total.append(0)
    timeseries_start.append(0)
    count_start.append(0)
    count_end.append(0)

for date2 in dates:
    object = datetime.strftime(datetime.strptime(date2,'%Y-%m-%d'), '%Y-%m-%d %H:%M:%S')
    dates3.append(object)
print("dates3 is done")

thiscase = [dates3[0]]
first = caseID[0]
for i in range(0, len(caseID)):
    if caseID[i] == first:
        thiscase.append(dates3[i])
    else:
        earliest = datetime.strptime(thiscase[0], '%Y-%m-%d %H:%M:%S')
        latest = datetime.strptime(thiscase[0], '%Y-%m-%d %H:%M:%S')
        for case in thiscase:
            case = datetime.strptime(case, '%Y-%m-%d %H:%M:%S')
            if case < earliest: earliest = case
            if case > latest: latest = case
        earliest = datetime.strftime(earliest, "%Y-%m-%d %H:%M:%S")
        latest = datetime.strftime(latest, "%Y-%m-%d %H:%M:%S")
        dur = datetime.strptime(latest, "%Y-%m-%d %H:%M:%S") - datetime.strptime(earliest, "%Y-%m-%d %H:%M:%S")
        duration = dur.days
        for j in range(0,len(single_dates)):
            if earliest == single_dates[j]:
                timeseries_start_total[j] = timeseries_start_total[j]+duration
                print(earliest)
                count_start[j] = count_start[j] + 1
            if latest == single_dates[j]:
                timeseries_end_total[j] = timeseries_end_total[j]+duration
                count_end[j] = count_end[j] + 1
        first = caseID[i]
        thiscase = [dates3[i]]
earliest = datetime.strptime(thiscase[0], '%Y-%m-%d %H:%M:%S')
latest = datetime.strptime(thiscase[0], '%Y-%m-%d %H:%M:%S')
for case in thiscase:
    case = datetime.strptime(case, '%Y-%m-%d %H:%M:%S')
    if case < earliest: earliest = case
    if case > latest: latest = case
earliest = datetime.strftime(earliest, "%Y-%m-%d %H:%M:%S")
latest = datetime.strftime(latest, "%Y-%m-%d %H:%M:%S")
dur = datetime.strptime(latest, "%Y-%m-%d %H:%M:%S") - datetime.strptime(earliest, "%Y-%m-%d %H:%M:%S")
duration = dur.days
for j in range(0, len(single_dates)):
    if earliest == single_dates[j]:
        timeseries_start_total[j] = timeseries_start_total[j] + duration
    if latest == single_dates[j]:
        timeseries_end_total[j] = timeseries_end_total[j] + duration

for i in range(0, len(timeseries_start)):
    if count_start[i]>0:
        timeseries_start[i] = timeseries_start_total[i]/count_start[i]
    else:
        timeseries_start[i] = 0

    if count_end[i]>0:
        x=1
        timeseries_end[i] = timeseries_end_total[i]/count_end[i]
    else:
        timeseries_end[i] = 0


with open(output_start,'w',newline='')as f:
    writer=csv.writer(f)
    temp = []
    temp.append("Date")
    temp.append("Duration Start")
    writer.writerow(temp)
    for i in range(0,len(timeseries_start)):
        temp = []
        temp.append(single_dates[i])
        temp.append(timeseries_start[i])
        writer.writerow(temp)
