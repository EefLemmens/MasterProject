#© Eef Lemmens

import re
import csv
import ast
from datetime import datetime
from datetime import timedelta, date

#Defining variables
dates = []
dates2 = []
dates3 = []
variant = []
single_dates = []
temp = []

#Traffic Fine
start_date =  date(2000, 1, 1)
end_date = date(2013, 6, 18)

#Input
inputfile = 'Road_Traffic_Fine_Management_Process.csv'
for line in open(inputfile, 'r').readlines():
    elements=line.split(';')
    row = [element.rstrip('\n') for element in elements]
    dates.append(row[3])
    variant.append(row[5])
dates.pop(0)
variant.pop(0)

#Functions
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#Make variant numbers into integers
for i in range(0,len(variant)):
    variant[i]=ast.literal_eval(variant[i])


#Find number of case variants
numberofvariants = 0
for number in variant:
    if number > numberofvariants:
        numberofvariants = number


#Fill lists
for single_date in daterange(start_date, end_date):
    single_dates.append(datetime.strftime(single_date,"%Y-%m-%d %H:%M:%S"))


a,b = len(single_dates),numberofvariants
Count = [[0 for x in range(b)] for y in range(a)]

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

#Count case variants at a certain date
for j in range(0,len(dates3)):
    for i in range(0, len(single_dates)):
        if dates3[j] == single_dates[i]:
            Count[i][variant[j]-1] += 1

numbercasevar = []
for i in range(0,len(single_dates)):
    numbercasevar.append(0)

for i in range(0, len(Count)):
    for j in range(0,len(Count[i])):
        if Count[i][j] > 0:
            numbercasevar[i] = numbercasevar[i] + 1

#Write count to csv file
with open('Number_Of_Case_Variant_Road_Traffic_Fine.csv','w', newline ='') as f:
    writer = csv.writer(f)
    for i in range(0,len(single_dates)):
        temp = [single_dates[i], numbercasevar[i]]
        writer.writerow(temp)
