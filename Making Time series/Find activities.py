#© Eef Lemmens

import csv

activities = []

inputfile = 'Sepsis_Cases.csv'
for line in open(inputfile, 'r').readlines():
    elements=line.split(';')
    row = [element.rstrip('\n') for element in elements]
    activities.append(row[1])
activities.pop(0)

print(len(activities))
distinct_activities = []
distinct_activities.append(activities[0])
for i in range(0, len(activities)):
    number = i
    print(i)
    for j in range(0,len(distinct_activities)):
        if distinct_activities[j] == activities[i]:
            continue
    distinct_activities.append(activities[i])
print(distinct_activities)

with open('Activities_Sepsis_Cases.csv','w',newline='')as f:
    writer=csv.writer(f)
    for i in range(0,len(distinct_activities)):
        temp=[distinct_activities[i]]
        writer.writerow(temp)
