#© Eef Lemmens

import csv
from datetime import datetime
from datetime import timedelta, date
from pandas import datetime as dt

#vectors
outlierdata = []
data = []
allactivities = []
outliercases = []
nonoutliercases = []

#input files
inputfile = 'Only Outliers Durationactivities BPI2017.csv'
for line in open(inputfile, 'r').readlines():
    elements=line.split(',')
    row = [element.rstrip('\n') for element in elements]
    outlierdata.append(row)

firstline = []

if inputfile == 'Only Outliers Durationactivities BPI2017.csv':
    caseID = []
    activity = []
    resource = []
    starttimestamp = []
    completetimestamp = []
    variantcase = []
    variant = []
    applicationtype = []
    loangoal = []
    requested_Amount = []
    accepted = []
    action = []
    creditscore = []
    eventID = []
    eventorigin = []
    firstwithdrawalamount = []
    monthlycost = []
    numberofterms = []
    offerID = []
    offeramount = []
    selected = []
    lifecycletransition = []


inputfile = 'BPI Challenge 2017.csv'
for line in open(inputfile, 'r').readlines():
    elements = line.split(';')
    row = [element.rstrip('\n') for element in elements]
    data.append(row)
    if inputfile == 'BPI Challenge 2017.csv':
        caseID.append(row[0])
        activity.append(row[1])
        resource.append(row[2])
        starttimestamp.append(row[3])
        completetimestamp.append(row[4])
        variantcase.append(row[5])
        variant.append(row[6])
        applicationtype.append(row[7])
        loangoal.append(row[8])
        requested_Amount.append(row[9])
        accepted.append(row[10])
        action.append(row[11])
        creditscore.append(row[12])
        eventID.append(row[13])
        eventorigin.append(row[14])
        firstwithdrawalamount.append(row[15])
        monthlycost.append(row[16])
        numberofterms.append(row[17])
        offerID.append(row[18])
        offeramount.append(row[19])
        selected.append(row[20])
        lifecycletransition.append(row[21])


if inputfile == 'BPI Challenge 2017.csv':
    firstline.append(caseID[0])
    firstline.append(activity[0])
    firstline.append(resource[0])
    firstline.append(starttimestamp[0])
    firstline.append(completetimestamp[0])
    firstline.append(variantcase[0])
    firstline.append(variant[0])
    firstline.append(applicationtype[0])
    firstline.append(loangoal[0])
    firstline.append(requested_Amount[0])
    firstline.append(accepted[0])
    firstline.append(action[0])
    firstline.append(creditscore[0])
    firstline.append(eventID[0])
    firstline.append(eventorigin[0])
    firstline.append(firstwithdrawalamount[0])
    firstline.append(monthlycost[0])
    firstline.append(numberofterms[0])
    firstline.append(offerID[0])
    firstline.append(offeramount[0])
    firstline.append(selected[0])
    firstline.append(lifecycletransition[0])

    caseID.pop(0)
    activity.pop(0)
    resource.pop(0)
    starttimestamp.pop(0)
    completetimestamp.pop(0)
    variantcase.pop(0)
    variant.pop(0)
    applicationtype.pop(0)
    loangoal.pop(0)
    requested_Amount.pop(0)
    accepted.pop(0)
    action.pop(0)
    creditscore.pop(0)
    eventID.pop(0)
    eventorigin.pop(0)
    firstwithdrawalamount.pop(0)
    monthlycost.pop(0)
    numberofterms.pop(0)
    offerID.pop(0)
    offeramount.pop(0)
    selected.pop(0)
    lifecycletransition.pop(0)

#Make dates from dates
completetimestamp2 = []
for date in completetimestamp:
    object = datetime.strftime(datetime.strptime(date,'%Y/%m/%d %H:%M:%S.%f'), '%Y-%m-%d')
    completetimestamp2.append(object)

outlierdates = []
for i in range(1, len(outlierdata)):
    outlierdata[i][0] = datetime.strftime(datetime.strptime(outlierdata[i][0],'%Y/%m/%d'), '%Y-%m-%d')
    outlierdates.append(object)

#Make floats
for i in range(1,len(outlierdata)):
    for j in range(1,len(outlierdata[i])):
        outlierdata[i][j] = int(outlierdata[i][j])

#Find case ID's that are outliers
for i in range(1,len(outlierdata)):
    for j in range(1, len(outlierdata[i])):
        if outlierdata[i][j] == 1:
            for k in range(0, len(caseID)):
                if completetimestamp2[k] == outlierdata[i][0]:
                    if caseID[k] not in outliercases:
                        outliercases.append(caseID[k])

#Find case ID's that are not outliers
for i in range(0,len(caseID)):
    if caseID[i] not in outliercases:
        nonoutliercases.append(caseID[i])

with open('Outliers file Durationactivities BPI2017.csv','w', newline ='') as f:
    writer = csv.writer(f)
    temp = []
    for i in range(0,len(firstline)):
        temp.append(firstline[i])
    writer.writerow(temp)
    for i in range(0, len(caseID)):
        if caseID[i] in outliercases:
            temp = []
            if inputfile == 'BPI Challenge 2017.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(resource[i])
                temp.append(starttimestamp[i])
                temp.append(completetimestamp[i])
                temp.append(variantcase[i])
                temp.append(variant[i])
                temp.append(applicationtype[i])
                temp.append(loangoal[i])
                temp.append(requested_Amount[i])
                temp.append(accepted[i])
                temp.append(action[i])
                temp.append(creditscore[i])
                temp.append(eventID[i])
                temp.append(eventorigin[i])
                temp.append(firstwithdrawalamount[i])
                temp.append(monthlycost[i])
                temp.append(numberofterms[i])
                temp.append(offerID[i])
                temp.append(offeramount[i])
                temp.append(selected[i])
                temp.append(lifecycletransition[i])
                writer.writerow(temp)

with open('NonOutliers file Durationactivities BPI2017.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    temp = []
    for i in range(0,len(firstline)):
        temp.append(firstline[i])
    writer.writerow(temp)
    for i in range(0, len(caseID)):
        if caseID[i] not in outliercases:
            temp = []
            if inputfile == 'BPI Challenge 2017.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(resource[i])
                temp.append(starttimestamp[i])
                temp.append(completetimestamp[i])
                temp.append(variantcase[i])
                temp.append(variant[i])
                temp.append(applicationtype[i])
                temp.append(loangoal[i])
                temp.append(requested_Amount[i])
                temp.append(accepted[i])
                temp.append(action[i])
                temp.append(creditscore[i])
                temp.append(eventID[i])
                temp.append(eventorigin[i])
                temp.append(firstwithdrawalamount[i])
                temp.append(monthlycost[i])
                temp.append(numberofterms[i])
                temp.append(offerID[i])
                temp.append(offeramount[i])
                temp.append(selected[i])
                temp.append(lifecycletransition[i])
                writer.writerow(temp)
