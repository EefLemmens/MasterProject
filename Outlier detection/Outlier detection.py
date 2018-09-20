#© Eef Lemmens

import csv
import numpy as np
import Classification as cf

inputfile = 'Events_Per_Day_Hospital_Billing.csv'
outputoutlier = 'Outliers Events Per Day Hospital Billing.csv'
outputonlyoutlier = 'Only Outliers Events Per Day Hospital Billing.csv'
#Define functions

#Z-score algorithm peaks
def zscore(temp,lag,threshold, influence):
    signals = np.zeros(len(temp))
    filtered_ts = np.array(temp)
    avg_filter = [0] * len(temp)
    std_filter = [0] * len(temp)
    avg_filter[lag - 1] = np.mean(temp[0:lag])
    std_filter[lag - 1] = np.std(temp[0:lag])

    for j in range(lag, len(temp)):
        if abs(temp[j] - avg_filter[j - 1]) > (threshold * std_filter[j - 1]):  # Look if there is a peak
            if (temp[j] - avg_filter[j - 1]) > (threshold * std_filter[j - 1]):  # Peak is above average
                signals[j] = 1
                filtered_ts[j] = influence * temp[j] + (1 - influence) * filtered_ts[j - 1]
            elif (avg_filter[j - 1] - temp[j]) > (threshold * std_filter[j - 1]):
                signals[j] = 1
                filtered_ts[j] = influence * temp[j] + (1 - influence) * filtered_ts[j - 1]
            # New time series to calculate average with
            avg_filter[j] = np.mean(filtered_ts[(j - lag):j])
            std_filter[j] = np.std(filtered_ts[(j - lag):j])
        else:
            signals[j] = 0
            filtered_ts[j] = temp[j]
            avg_filter[j] = np.mean(filtered_ts[(j - lag):j])
            std_filter[j] = np.std(filtered_ts[(j - lag):j])

    return signals

histograms = []

#Input data

for line in open(inputfile, 'r').readlines():
    elements=line.split(',')
    row = [element.rstrip('\n') for element in elements]
    histograms.append(row)

#Make floats of inputdata
for i in range(1,len(histograms)):
    for j in range(1,len(histograms[i])):
        histograms[i][j] = float(histograms[i][j])

#Make outlier matrix
outliers = []
for i in range(0, len(histograms)):
    outliers.append([])
    for j in range(0,len(histograms[i])):
        outliers[i].append(0)

outliers[0] = histograms[0]
for i in range(1, len(histograms)):
    outliers[i][0] = histograms[i][0]

#Define variables
lag = 60
threshold1 = 2
influence1 = 0.2
threshold2 = 10
influence2 = 0.1
threshold3 = 30
influence3 = 0


for i in range(1, len(histograms[0])):
    check = 0
    temp = []
    for j in range(1, len(histograms)):
        temp.append(histograms[j][i])
    answer = cf.classify(temp, check)
    check = answer

    #Peaks
    if answer == "Peaks":
        print(histograms[0][i], "Peaks")
        #Z-score algorithm
        signals = zscore(temp, lag, threshold1, influence1)
        for j in range(0,len(signals)):
            if signals[j] == 1:
                outliers[j+1][i] = 1
            elif signals[j] == 0:
                outliers[j+1][i] = 0

    if answer == "Peaks2":
        print(histograms[0][i], "Peaks2")
        #Z-score algorithm
        signals = zscore(temp, lag, threshold2, influence2)
        for j in range(0,len(signals)):
            if signals[j] == 1:
                outliers[j+1][i] = 1
            elif signals[j] == 0:
                outliers[j+1][i] = 0

    if answer == "Random":
        print(histograms[0][i], "Random")
        # Z-score algorithm
        if len(temp)>lag:
            signals = zscore(temp, lag, threshold1, influence1)
            for j in range(0, len(signals)):
                if signals[j] == 1:
                    outliers[j + 1][i] = 1
                elif signals[j] == 0:
                    outliers[j + 1][i] = 0

            #outliers[j+1][i] = signals[j]


    if answer == "Few Values":
        print(histograms[0][i], "Few values")
        for j in range(0,len(temp)):
            if temp[j] > 0:
                outliers[j+1][i] = 1
            else:
                outliers[j+1][i] = 0

    if answer == "Smooth":
        print(histograms[0][i], "Smooth")
        above = 0
        below = 0
        firstabove = 0
        firstbelow = 0
        average = np.mean(temp)
        standarddeviation = np.std(temp)
        averageplus = average + standarddeviation
        averageminus = average - standarddeviation
        for j in range(0,len(temp)):
            if temp[j]>=average and temp[j-1]<average:
                above = above + 1
                firstabove = j
                if below > 5:
                    averagepeak = np.mean(temp[firstbelow:j])
                    if averagepeak < averageminus:
                        for k in range(firstbelow,j):
                            if temp[k]<averageminus:
                                outliers[k+1][i] = 1
                below = 0
            elif temp[j]<average and temp[j-1]>average:
                below = below + 1
                firstbelow = j
                if above > 5:
                    averagepeak = np.mean(temp[firstabove:j])
                    if averagepeak > averageplus:
                        for k in range(firstabove, j):
                            if temp[k] > averageplus:
                                outliers[k+1][i] = 1
                above = 0
            elif temp[j]>=average:
                above = above + 1
            elif temp[j]<average:
                below = below + 1
            else:
                print("Did I do something wrong here? Make a long sentence so it stands out")

        if above > 5:
            averagepeak = np.mean(temp[firstabove:j])
            if averagepeak > averageplus:
                for k in range(firstabove, j+1):
                    if temp[k] > averageplus:
                        outliers[k+1][i] = 1
        if below > 5:
            averagepeak = np.mean(temp[firstbelow:j])
            if averagepeak < averageminus:
                for k in range(firstbelow, j+1):
                    if temp[k] < averageminus:
                        outliers[k+1][i] = 1

    if answer == "Weekly":
        print(histograms[0][i], "Weekly")
        period = 7
        days = []
        answer2 = cf.classify(temp, check)
        for j in range(0,period):
            days.append([])
        outliertemp = []
        for j in range(0,period):
            outliertemp.append([])
        for j in range(0, len(temp)):
            day = j%period
            days[day].append(temp[j])
            outliertemp[day].append(0)
        for j in range(0,len(days)):
            temp2 = []
            for k in range(0,len(days[j])):
                temp2.append(days[j][k])
            answer = cf.classify(temp2, check)
            if answer == "Peaks":
                print("Weekly Peaks")
                signals = zscore(temp2,lag,threshold1,influence1)
                for k in range(0,len(signals)):
                    if signals[k] == 1:
                        outliertemp[j][k] = 1
                    elif signals[k] == 0:
                        outliertemp[j][k] = 0
            if answer == "Peaks2":
                print("Weekly Peaks2")
                signals = zscore(temp2, lag, threshold2, influence2)
                for k in range(0, len(signals)):
                    if signals[k] == 1:
                        outliertemp[j][k] = 1
                    elif signals[k] == 0:
                        outliertemp[j][k] = 0
            if answer == "Few Values":
                print("Weekly Few Values")
                for k in range(0, len(temp2)):
                    if temp2[k] > 0:
                        outliertemp[j][k] = 1
            if answer == "Weekly":
                print("Weekly Weekly, something went wrong")
            if answer == "Monthly":
                print("Weekly Monthly, something went wrong")
            if answer == "Smooth":
                print("Weekly Smooth")
                above = 0
                below = 0
                firstabove = 0
                firstbelow = 0
                average = np.mean(temp2)
                standarddeviation = np.std(temp2)
                averageplus = average + standarddeviation
                averageminus = average - standarddeviation
                for m in range(0, len(temp2)):
                    if temp2[m] >= average and temp2[m - 1] < average:
                        above = above + 1
                        firstabove = m
                        if below > 5:
                            averagepeak = np.mean(temp2[firstbelow:m])
                            if averagepeak < averageminus:
                                for n in range(firstbelow, m):
                                    if temp2[n] < averageminus:
                                        outliertemp[j][n] = 1
                        below = 0
                    elif temp2[m] < average and temp2[m - 1] > average:
                        below = below + 1
                        firstbelow = j
                        if above > 5:
                            averagepeak = np.mean(temp[firstabove:m])
                            if averagepeak > averageplus:
                                for n in range(firstabove, m):
                                    if temp2[n] > averageplus:
                                        outliertemp[j][n] = 1
                        above = 0
                    elif temp2[m] >= average:
                        above = above + 1
                    elif temp2[m] < average:
                        below = below + 1
                    else:
                        print("Did I do something wrong here? Make a long sentence so it stands out")
                if above > 5:
                    averagepeak = np.mean(temp[firstabove:m])
                    if averagepeak > averageplus:
                        for n in range(firstabove, m+1):
                            if temp[n] > averageplus:
                                outliertemp[j][n] = 1
                                print("done something above")
                if below > 5:
                    averagepeak = np.mean(temp2[firstbelow:m])
                    if averagepeak < averageminus:
                        for n in range(firstbelow, m+1):
                            if temp[n] < averageminus:
                                outliertemp[j][n] = 1
                                print("done something below")
            if answer == "Random":
                print("Weekly Random")
                # Z-score algorithm
                if len(temp2)>lag:
                    signals = zscore(temp2, lag, threshold1, influence1)
                    for k in range(0, len(signals)):
                        if signals[k] == 1:
                            outliertemp[j][k] = 1
                        elif signals[k] == 0:
                            outliertemp[j][k] = 0
                else:
                    signals = zscore(temp2, 10, threshold1, influence1)
                    for k in range(0, len(signals)):
                        if signals[k] == 1:
                            outliertemp[j][k] = 1
                        elif signals[k] == 0:
                            outliertemp[j][k] = 0

        #Compine outliertemp

        for n in range(0,len(days)):
            number = n%period
            for k in range(0,len(days[n])):
                if outliertemp[n][k] == 1:
                    outliers[number+k*7+1][i] = 1

                elif outliertemp[n][k] == 0:
                    outliers[number+k*7+1][i] = 0

        #Check if time series also has clear peaks
        if answer2 == "Peaks2":
            print("Weekly and Peaks2")
            signals = zscore(temp, lag, threshold2, influence2)
            for j in range(0, len(signals)):
                if signals[j] == 1 and outliers[j + 1][i] == 0:
                    outliers[j + 1][i] = 1
                elif signals[j] == 1 and outliers[j+1][i] == 1:
                    outliers[j+1][i] = 1
                elif signals[j] == 0 and outliers[j + 1][i] == 0:
                    outliers[j + 1][i] = 0
                elif signals[j] == 0 and outliers[j+1][i] == 1:
                    outliers[j+1][i] = 1
                else:
                    print("Er is iets misgegaan in weekly and peaks2")

        if answer2 == "Peaks":
            print("Weekly and Peaks")
            signals = zscore(temp, lag, threshold1, influence1)
            for j in range(0, len(signals)):
                if signals[j] == 1 and outliers[j + 1][i] == 0:
                    outliers[j + 1][i] = 1
                elif signals[j] == 1 and outliers[j+1][i] ==1:
                    outliers[j+1][i] = 1
                elif signals[j] == 0 and outliers[j + 1][i] == 0:
                    outliers[j + 1][i] = 0
                elif signals[j] == 0 and outliers[j+1][i] == 1:
                    outliers[j+1][i] = 0
                else: print("Er is iets misgegaan in weekly and peaks")
        if answer2 == "Peaks3":
            print("Weekly and Peaks3")
            signals = zscore(temp, lag, threshold3, influence3)
            for j in range(0, len(signals)):
                if signals[j] == 1 and outliers[j + 1][i] == 0:
                    outliers[j + 1][i] = 1
                elif signals[j] == 1 and outliers[j+1][i] == 1:
                    outliers[j+1][i] = 1
                elif signals[j] == 0 and outliers[j + 1][i] == 0:
                    outliers[j + 1][i] = 0
                elif signals[j] == 0 and outliers[j+1][i] == 1:
                    outliers[j+1][i] = 0
                else: print("Er is iets misgegaan in weekly and peaks3")


    if answer == "Monthly":
        print(histograms[0][i], "Monthly")
        period = 30
        # days = [[] for x in range(period)]
        # for j in range(0, len(temp)):
        #     day = j % period
        #     days[day].append(temp[j])
        # for j in range(0, len(days)):
        #     temp2 = []
        #     for k in range(0, len(days[j])):
        #         temp2.append(days[j][k])
        #     answer = cf.classify(temp2, check)
        days = []
        for j in range(0,period):
            days.append([])
        outliertemp = []
        for j in range(0,period):
            outliertemp.append([])
        for j in range(0, len(temp)):
            day = j%period
            days[day].append(temp[j])
            outliertemp[day].append(0)
        for j in range(0,len(days)):
            temp2 = []
            for k in range(0,len(days[j])):
                temp2.append(days[j][k])
            answer = cf.classify(temp2, check)
            if answer == "Peaks":
                print("Monthly Peaks")
                signals = zscore(temp2,lag,threshold1,influence1)
                for k in range(0,len(signals)):
                    outliertemp[j][k] = signals [k]
            if answer == "Few Values":
                print("Monthly Few Values")
                for k in range(0, len(temp2)):
                    if temp2[k] > 0:
                        outliertemp[j][k] = 1
            if answer == "Weekly":
                print("Monthly Weekly, something went wrong")
            if answer == "Monthly":
                print("Monthly Monthly, something went wrong")
            if answer == "Smooth":
                print("Monthly Smooth")
                above = 0
                below = 0
                firstabove = 0
                firstbelow = 0
                average = np.mean(temp2)
                standarddeviation = np.std(temp2)
                averageplus = average + standarddeviation
                averageminus = average - standarddeviation
                for m in range(0, len(temp2)):
                    if temp2[m] >= average and temp2[m - 1] < average:
                        above = above + 1
                        firstabove = m
                        if below > 5:
                            averagepeak = np.mean(temp2[firstbelow:m])
                            if averagepeak < averageminus:
                                for n in range(firstbelow, m):
                                    if temp[n] < averageminus:
                                        outliertemp[j][n] = 1
                                        print("done something below")
                        below = 0
                    elif temp[i] < average and temp[i - 1] > average:
                        below = below + 1
                        firstbelow = j
                        if above > 5:
                            averagepeak = np.mean(temp[firstabove:m])
                            if averagepeak > averageplus:
                                for n in range(firstabove, m):
                                    if temp[n] > averageplus:
                                        outliertemp[j][n] = 1
                                        print("done something above")
                        above = 0
                    elif temp[i] >= average:
                        above = above + 1
                    elif temp[i] < average:
                        below = below + 1
                    else:
                        print("Did I do something wrong here? Make a long sentence so it stands out")


        for n in range(0,len(days)):
            number = n%period
            for k in range(0,len(days[n])):
                outliers[number + k*7+1][i] = outliertemp[n][k]
            #Combine outliertemp

        histograms[0][0]= "Date"

        #Write to CSV
with open(outputoutlier,'w', newline ='') as f:
    writer = csv.writer(f)
    for i in range(0, len(histograms)):
        temp = []
        temp.append(histograms[i][0])
        for j in range(1, len(histograms[i])):
            temp.append(histograms[i][j])
            temp.append(outliers[i][j])
        writer.writerow(temp)

with open(outputonlyoutlier,'w', newline ='') as f:
    writer = csv.writer(f)
    for i in range(0, len(histograms)):
        temp = []
        temp.append(histograms[i][0])
        for j in range(1, len(histograms[i])):
            temp.append(outliers[i][j])
        writer.writerow(temp)
