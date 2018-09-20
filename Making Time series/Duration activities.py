#© Eef Lemmens

import csv
from datetime import datetime
from datetime import timedelta, date

inputfile = 'BPI Challenge 2017.csv'
inputfile2 = 'Activities_BPI2017.csv'

start_date =  date(2016, 1, 1)
end_date = date(2017, 12, 31)



starttime = []
endtime = []
activity = []
duration_in_s = []
single_dates = []
starttime2 = []
endtime2 = []
adding = []
activities = []
addingmatrix = []


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#Fill lists
for single_date in daterange(start_date, end_date):
    single_dates.append(datetime.strftime(single_date,"%Y/%m/%d"))

for i in range(0,len(single_dates)):
    adding.append(0)

for line in open(inputfile, 'r').readlines():
    elements=line.split(';')
    row = [element.rstrip('\n') for element in elements]
    activity.append(row[1])
    starttime.append(row[3])
    endtime.append(row[4])

activity.pop(0)
starttime.pop(0)
endtime.pop(0)

for line in open(inputfile2, 'r').readlines():
    elements=line.split(';')
    row = [element.rstrip('\n') for element in elements]
    activities.append(row[0])


for i in range(0,len(starttime)):
    objects1 = datetime.strftime(datetime.strptime(starttime[i], '%Y/%m/%d %H:%M:%S.%f'), '%Y/%m/%d')
    objects = datetime.strptime(starttime[i], '%Y/%m/%d %H:%M:%S.%f')
    starttime[i] = objects
    starttime2.append(objects1)
    objecte1 = datetime.strftime(datetime.strptime(endtime[i], '%Y/%m/%d %H:%M:%S.%f'), '%Y/%m/%d')
    objecte = datetime.strptime(endtime[i], '%Y/%m/%d %H:%M:%S.%f' )
    endtime[i] = objecte
    endtime2.append(objecte1)

for i in range(0,len(starttime)):
    duration= endtime[i]-starttime[i]
    temp = duration.total_seconds()
    temp = int(temp)
    duration_in_s.append(temp)

count = []
average = []
for i in range(0, len(single_dates)):
    count.append(0)
    average.append(0)

for i in range(0, len(endtime)):
    for j in range(0, len(single_dates)):
        if endtime2[i] == single_dates[j]:
            adding[j] = adding[j] + duration_in_s[i]
            count[j] = count[j] + 1

for i in range(0, len(single_dates)):
    if adding[i]>0:
        average[i] = adding[i]/count[i]

with open('Durationactivities_BPI2017.csv','w',newline='')as f:
    writer=csv.writer(f)
    temp2 = []
    temp2.append("Date")
    temp2.append("Number")
    writer.writerow(temp2)
    for i in range(0,len(single_dates)):
        temp=[]
        temp.append(single_dates[i])
        temp.append(average[i])
        writer.writerow(temp)


#Per activity
for i in range(0,len(single_dates)):
    addingmatrix.append([])
    for j in range(0,len(activities)):
        addingmatrix[i].append(0)

countmatrix = []
averagematrix = []
for i in range(0, len(single_dates)):
    countmatrix.append([])
    averagematrix.append([])
    for j in range(0,len(activities)):
        countmatrix[i].append(0)
        averagematrix[i].append(0)


for j in range(0,len(endtime)):
    for k in range(0,len(single_dates)):
        if endtime2[j] == single_dates[k]:
            for m in range(0, len(activities)):
                if activities[m] == activity[j]:
                    addingmatrix[k][m] = addingmatrix[k][m]+duration_in_s[j]
                    countmatrix[k][m] = countmatrix[k][m]+1

for i in range(0, len(single_dates)):
    for j in range(0,len(activities)):
            if addingmatrix[i][j]>0:
                averagematrix[i][j] = addingmatrix[i][j]/countmatrix[i][j]

with open('Durationactivities_Per_Activity_BPI2017.csv','w',newline='')as f:
    writer=csv.writer(f)
    temp2 = []
    temp2.append("Date")
    for act in activities:
        temp2.append(act)
    writer.writerow(temp2)
    for i in range(0,len(single_dates)):
        temp=[]
        temp.append(single_dates[i])
        for j in range(0,len(activities)):
            temp.append(averagematrix[i][j])
        writer.writerow(temp)
