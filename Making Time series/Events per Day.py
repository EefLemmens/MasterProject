#Importing libraries
import re
import csv
from datetime import datetime
from datetime import timedelta, date

#Setting variables
dates = []
dates2 = []
dates3 = []
single_dates = []
count = []
temp = []

#sepsis
start_date = date(2000, 11, 7)
end_date = date(2013, 6, 5)

#Functions
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#Fill lists
for single_date in daterange(start_date, end_date):
    single_dates.append(datetime.strftime(single_date,"%Y-%m-%d %H:%M:%S"))

for i in range(0,len(single_dates)):
    count.append(0)

#Input
inputfile = 'Road_Traffic_Fine_Management_Process.csv'
for line in open(inputfile, 'r').readlines():
    elements=line.split(';')
    row = [element.rstrip('\n') for element in elements]
    dates.append(row[2])
dates.pop(0)

#Make data usable
for date in dates:
    list = re.findall(".", date)
    list.pop(22)
    list.pop(21)
    list.pop(20)
    list.pop(19)
    list.pop(18)
    list.pop(17)
    list.pop(16)
    list.pop(15)
    list.pop(14)
    list.pop(13)
    list.pop(12)
    list.pop(11)
    list.pop(10)
    list2 =''.join(list)
    dates2.append(list2)

for date2 in dates2:
    object = datetime.strftime(datetime.strptime(date2,'%Y/%m/%d'), '%Y-%m-%d %H:%M:%S')
    dates3.append(object)

#Count number of events at a certain date
for date3 in dates3:
    for i in range(0, len(single_dates)):
        if date3 == single_dates[i]:
            count[i] += 1

#Write count to csv file
with open('Count_Road_Traffic_Fine.csv','w', newline ='') as f:
    writer = csv.writer(f)
    for i in range(0,len(count)):
        temp = [single_dates[i],count[i]]
        writer.writerow(temp)



