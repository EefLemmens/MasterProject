#© Eef Lemmens

import re
import csv
import ast
from datetime import datetime
from datetime import timedelta, date
from pandas import datetime as dt

#Defining variables
dates = []
dates2 = []
dates3 = []
single_dates = []
temp = []
caseID = []
duration = []
earliestdates = []
latestdates = []
distactivities = []
activities = []


start_date =  date(2016, 1, 1)
end_date = date(2017, 12, 31)

#Input
inputfile = 'BPI_Challenge_2017_2.csv'
for line in open(inputfile, 'r').readlines():
    elements=line.split(';')
    row = [element.rstrip('\n') for element in elements]
    caseID.append(row[0])
    activities.append(row[1])
    dates.append(row[3])
dates.pop(0)
caseID.pop(0)
activities.pop(0)

inputfile = 'Activities_BPI2017.csv'
for line in open(inputfile, 'r').readlines():
    elements=line.split(';')
    row = [element.rstrip('\n') for element in elements]
    distactivities.append(row[0])

#Functions
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#Fill lists
for single_date in daterange(start_date, end_date):
    single_dates.append(datetime.strftime(single_date,"%Y-%m-%d %H:%M:%S"))

#Make data usable


print("dates2 is done")

for date2 in dates:
    object = datetime.strftime(datetime.strptime(date2,'%Y-%m-%d'), '%Y-%m-%d %H:%M:%S')
    dates3.append(object)
print("dates3 is done")



count = 1
for i in range(1,len(caseID)):
    if caseID[i] != caseID[i-1]:
        count = count + 1

caseIDused = []
for i in range(count):
    caseIDused.append(0)
    duration.append(0)
    earliestdates.append(0)
    latestdates.append(0)
thiscase = [dates3[0]]
first = caseID[0]
count2 = 0
for i in range(1,len(caseID)):
    if caseID[i] == first:
        thiscase.append(dates3[i])
    else:
        caseIDused[count2] = caseID[i-1]
        earliest = datetime.strptime(thiscase[0], '%Y-%m-%d %H:%M:%S')
        latest = datetime.strptime(thiscase[0], '%Y-%m-%d %H:%M:%S')
        for case in thiscase:
            case = datetime.strptime(case, '%Y-%m-%d %H:%M:%S')
            if case < earliest: earliest = case
            if case > latest: latest = case
        earliest = datetime.strftime(earliest, "%Y-%m-%d %H:%M:%S")
        latest = datetime.strftime(latest, "%Y-%m-%d %H:%M:%S")
        dur = datetime.strptime(latest, "%Y-%m-%d %H:%M:%S") - datetime.strptime(earliest, "%Y-%m-%d %H:%M:%S")
        duration[count2] = dur.days
        earliestdates[count2] = earliest
        latestdates[count2] = latest
        thiscase = [dates3[i]]
        first = caseID[i]
        count2 = count2 + 1

caseIDused[-1] = caseID[-1]

earliest = datetime.strptime(thiscase[0], '%Y-%m-%d %H:%M:%S')
latest = datetime.strptime(thiscase[0], '%Y-%m-%d %H:%M:%S')
for case in thiscase:
    case = datetime.strptime(case, '%Y-%m-%d %H:%M:%S')
    if case < earliest: earliest = case
    if case > latest: latest = case
earliest = datetime.strftime(earliest, "%Y-%m-%d %H:%M:%S")
latest = datetime.strftime(latest, "%Y-%m-%d %H:%M:%S")
dur = datetime.strptime(latest, "%Y-%m-%d %H:%M:%S") - datetime.strptime(earliest, "%Y-%m-%d %H:%M:%S")
duration[-1] = dur.days
earliestdates[-1] = earliest[-1]
latestdates[-1] = latest[-1]
# earliest = datetime.strptime(thiscase[0], '%Y-%m-%d %H:%M:%S')
# latest = datetime.strptime(thiscase[0], '%Y-%m-%d %H:%M:%S')
# for case in thiscase:
#     case = datetime.strptime(case, '%Y-%m-%d %H:%M:%S')
#     if case < earliest: earliest = case
#     if case > latest: latest = case
#     earliest = datetime.strftime(earliest, "%Y-%m-%d %H:%M:%S")
#     latest = datetime.strftime(latest, "%Y-%m-%d %H:%M:%S")
#     dur = datetime.strptime(latest, "%Y-%m-%d %H:%M:%S") - datetime.strptime(earliest, "%Y-%m-%d %H:%M:%S")
#     duration.append(dur.days)
#     earliestdates.append(earliest)
#     latestdates.append(latest)
print("Average duration uitrekenen")

#Find number of cases for every activity
thisone = [[] for x in range(len(distactivities))]
datesactivities = [[] for y in range(len(distactivities))]
first1 = caseID[0]
for i in range(0, len(activities)):
    for j in range(0,len(distactivities)):
        if activities[i] == distactivities[j]:
            thisone[j].append(caseID[i])
            datesactivities[j].append(dates3[i])

#Dubbelen eruit halen
# dubbelen = []
# counter = 0
# for i in range(0, len(thisone)):
#     for j in range(0, len(thisone[i])-1):
#         for k in range(1,len(thisone[i])):
#             if thisone[i][j] == thisone[i][k]:
#                 dubbelen.append(k)
#                 counter = counter + 1
#     print("One done")
#     for l in range(len(k), -1, -1):
#         thisone[i].pop(k)
#         datesactivities[i].pop(k)
#     print(i)
# print(counter)


print("Weer een stapje gedaan")

#Calculate average on one date


for i in range(0,len(distactivities)):
    for j in range(0,len(thisone[i])):
        for k in range(0,len(caseIDused)):
            if thisone[i][j] == caseIDused[k]:
                thisone[i][j] = k
    print(i, " i is gedaan")

print("This one is gemaakt")



#     else:
#         av_duration.append("NONE")

# av_duration_last = []
# for j in range(0,len(single_dates)):
#     temporary = 0
#     counter = 0
#     for i in range(0,len(duration)):
#         if latestdates[i] == single_dates[j]:
#             temporary = temporary + duration[i]
#             counter = counter +1
#     if counter > 0:
#         av_duration_last.append(temporary/counter)
#     else:
#         av_duration_last.append("NONE")

print("Ik ga schrijven")

#Scrijven naar CSV
with open('Thisone_BPI2017.csv','w',newline='')as f:
    writer=csv.writer(f)
    for i in range(0,len(thisone)):
        temp=[]
        for j in range(0,len(thisone[i])):
            temp.append(thisone[i][j])
        writer.writerow(temp)



    # for i in range(0,len(single_dates)):
    #     temp = [single_dates[i]]
    #     for j in range(0,len(Count[i])):
    #         temp.append(Count[i][j])
    #     writer.writerow(temp)
with open('Dur_For_Now_BPI2017.csv','w',newline='')as f:
    writer=csv.writer(f)
    for i in range(0,len(duration)):
        temp=[duration[i]]
        writer.writerow(temp)

with open('Datesactivities_BPI2017.csv','w',newline='')as f:
    writer=csv.writer(f)
    for i in range(0,len(datesactivities)):
        temp=[]
        for j in range(0,len(datesactivities[i])):
            temp.append(datesactivities[i][j])
        writer.writerow(temp)
