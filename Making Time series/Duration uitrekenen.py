#© Eef Lemmens

import csv
from datetime import datetime
from datetime import timedelta, date
import ast

single_dates = []
distactivities = []
datesactivities = []
av_durations = []
thisone = []
duration = []


with open('Thisone_BPI2012.csv') as csvthis:
    csvReader = csv.reader(csvthis)
    for row in csvReader:
        thisone.append(row)

with open('Dur_For_Now_BPI2012.csv') as csvdur:
    csvReader = csv.reader(csvdur)
    for row in csvReader:
        duration.append(row[0])

with open('Datesactivities_BPI2012.csv') as csvdates:
    csvReader = csv.reader(csvdates)
    for row in csvReader:
        datesactivities.append(row)

with open('Activities_BPI2012.csv') as csvact:
    csvReader = csv.reader(csvact)
    for row in csvReader:
        distactivities.append(row)

for i in range(0, len(thisone)):
    for j in range(0,len(thisone[i])):
        thisone[i][j] = ast.literal_eval(thisone[i][j])

for i in range(0, len(duration)):
    duration[i] = ast.literal_eval(duration[i])

for i in range(0, len(datesactivities)):
    for j in range(0, len(datesactivities[i])):
        datesactivities[i][j] = datetime.strftime(datetime.strptime(datesactivities[i][j], '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

start_date = date(2011, 10, 1)
end_date = date(2012, 3, 14)

#Hospital billing
# start_date =  date(2012, 12, 13)
# end_date = date(2016, 1, 19)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#Fill lists
for single_date in daterange(start_date, end_date):
    single_dates.append(datetime.strftime(single_date,"%Y-%m-%d %H:%M:%S"))

for i in range(0,len(single_dates)):
    av_durations.append([])
    for j in range(0,len(distactivities)):
        av_durations[i].append(0)

print("Average uitrekenen")
for i in range(0,len(thisone)):
    for j in range(0, len(single_dates)):
        temporary = 0
        counter = 0
        for k in range(0,len(thisone[i])):
            if datesactivities[i][k] == single_dates[j]:
                temporary = temporary +duration[thisone[i][k]]
                counter = counter +1
        if counter > 0:
            av_durations[j][i] = temporary/counter
        else:
            av_durations[j][i] = "None"
    print(i)

for row in av_durations:
    print(row)

print("Schrijven")
with open('Duration_BPI2012.csv','w',newline='')as f:
    writer=csv.writer(f)
    temp1 = [0]
    for i in range(0,len(distactivities)):
        temp1.append(distactivities[i])
    writer.writerow(temp1)
    for i in range(0,len(av_durations)):
        temp=[single_dates[i]]
        for j in range(0,len(av_durations[i])):
            temp.append(av_durations[i][j])
        writer.writerow(temp)
