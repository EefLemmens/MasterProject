#© Eef Lemmens

import csv
import numpy as np
import pylab
import pandas as pd


# Define functions
def compareWeek(first, second, answer):
    if answer != "Weekly":
        if first < second:
            average = (second - first)
            if average > second / 2:
                answer = "Weekly"
        if second < first:
            average = (first - second)
            if average > first / 2:
                answer = "Weekly"
    return answer

def compareMonth(first, second, answer):
    if answer != "Monthly":
        if answer != "Weekly":
            if first < second:
                average = (second - first)
                if average > second / 2:
                    answer = "Monthly"
            if second < first:
                average = (first - second)
                if average > first / 2:
                    answer = "Monthly"
    return answer

def classify(histogram, check):
    #Define variables
    period = 7
    period2 = 30
    thresholdFewValues = 0.05
    thresholdPeaks = 2
    thresholdPeaks2 = 10
    thresholdPeaks3 = 30
    thresholdPeaksNumber = 30
    lowerthresholdPeaksNumber = 3
    lagPeaks = 60
    influencePeaks = 0.2
    influencePeaks2 = 0.1
    influencePeaks3 = 0
    final = 0


    #Smooth
    meansmooth = np.mean(histogram)
    stdsmooth = np.std(histogram)
    checksmooth = 0

    for j in range(1,len(histogram)):
        if histogram[j]>histogram[j-1]+1.5*stdsmooth:
            checksmooth=checksmooth + 1
        elif histogram[j]<histogram[j-1]-1.5*stdsmooth:
            checksmooth=checksmooth +1

    #Few values
    countFewValues = 0
    for j in range(1,len(histogram)):
        if histogram[j] > 0:
            countFewValues = countFewValues + 1
    percentage = countFewValues/len(histogram)

    #Peaks3
    if len(histogram)>lagPeaks:
        countPeaks3 = 0
        filtered_ts = np.array(histogram)
        avg_filter = [0] * len(histogram)
        std_filter = [0] * len(histogram)
        avg_filter[lagPeaks - 1] = np.mean(histogram[0:lagPeaks])
        std_filter[lagPeaks - 1] = np.std(histogram[0:lagPeaks])
        for j in range(lagPeaks, len(histogram)):
            if abs(histogram[j] - avg_filter[j - 1]) > (thresholdPeaks3 * std_filter[j - 1]):  # Look if there is a peak
                if (histogram[j] - avg_filter[j - 1]) > (thresholdPeaks3 * std_filter[j - 1]):  # Peak is above average
                    countPeaks3 = countPeaks3 + 1
                    filtered_ts[j] = influencePeaks3 * histogram[j] + (1 - influencePeaks3) * filtered_ts[j - 1]
                elif (histogram[j] - avg_filter[j - 1]) < (thresholdPeaks3 * std_filter[j - 1]):  # Peak is below average
                    countPeaks3 = countPeaks3 + 1
                    filtered_ts[j] = influencePeaks3 * histogram[j] + (1 - influencePeaks3) * filtered_ts[j - 1]
                # New time series to calculate average with
                avg_filter[j] = np.mean(filtered_ts[(j - lagPeaks):j])
                std_filter[j] = np.std(filtered_ts[(j - lagPeaks):j])
            else:
                filtered_ts[j] = histogram[j]
                avg_filter[j] = np.mean(filtered_ts[(j - lagPeaks):j])
                std_filter[j] = np.std(filtered_ts[(j - lagPeaks):j])
    #Peaks
    if len(histogram) > lagPeaks:
        countPeaks = 0

        filtered_ts = np.array(histogram)
        avg_filter = [0] * len(histogram)
        std_filter = [0] * len(histogram)
        avg_filter[lagPeaks - 1] = np.mean(histogram[0:lagPeaks])
        std_filter[lagPeaks - 1] = np.std(histogram[0:lagPeaks])
        for j in range(lagPeaks, len(histogram)):
            if abs(histogram[j] - avg_filter[j - 1]) > (thresholdPeaks * std_filter[j - 1]):  # Look if there is a peak
                if (histogram[j] - avg_filter[j - 1]) > (thresholdPeaks * std_filter[j - 1]):  # Peak is above average
                    countPeaks = countPeaks + 1
                    filtered_ts[j] = influencePeaks * histogram[j] + (1 - influencePeaks) * filtered_ts[j - 1]
                elif (histogram[j] - avg_filter[j - 1]) < (thresholdPeaks * std_filter[j - 1]):  # Peak is below average
                    countPeaks = countPeaks + 1
                    filtered_ts[j] = influencePeaks * histogram[j] + (1 - influencePeaks) * filtered_ts[j - 1]
                # New time series to calculate average with
                avg_filter[j] = np.mean(filtered_ts[(j - lagPeaks):j])
                std_filter[j] = np.std(filtered_ts[(j - lagPeaks):j])
            else:
                filtered_ts[j] = histogram[j]
                avg_filter[j] = np.mean(filtered_ts[(j - lagPeaks):j])
                std_filter[j] = np.std(filtered_ts[(j - lagPeaks):j])
    #Peaks2
    if len(histogram)>lagPeaks:
        countPeaks2 = 0
        filtered_ts = np.array(histogram)
        avg_filter = [0] * len(histogram)
        std_filter = [0] * len(histogram)
        avg_filter[lagPeaks - 1] = np.mean(histogram[0:lagPeaks])
        std_filter[lagPeaks - 1] = np.std(histogram[0:lagPeaks])
        for j in range(lagPeaks, len(histogram)):
            if abs(histogram[j] - avg_filter[j - 1]) > (thresholdPeaks2 * std_filter[j - 1]):  # Look if there is a peak
                if (histogram[j] - avg_filter[j - 1]) > (thresholdPeaks2 * std_filter[j - 1]):  # Peak is above average
                    countPeaks2 = countPeaks2 + 1
                    filtered_ts[j] = influencePeaks2 * histogram[j] + (1 - influencePeaks2) * filtered_ts[j - 1]
                elif (histogram[j] - avg_filter[j - 1]) < (thresholdPeaks2 * std_filter[j - 1]):  # Peak is below average
                    countPeaks2 = countPeaks2 + 1
                    filtered_ts[j] = influencePeaks2 * histogram[j] + (1 - influencePeaks2) * filtered_ts[j - 1]
                # New time series to calculate average with
                avg_filter[j] = np.mean(filtered_ts[(j - lagPeaks):j])
                std_filter[j] = np.std(filtered_ts[(j - lagPeaks):j])
            else:
                filtered_ts[j] = histogram[j]
                avg_filter[j] = np.mean(filtered_ts[(j - lagPeaks):j])
                std_filter[j] = np.std(filtered_ts[(j - lagPeaks):j])






    #Week pattern
    if len(histogram) > period:
        if check != "Weekly":
            if check != "Monthly":
                bin = []
                average = []
                count = []
                for k in range(0,period):
                    bin.append(0)
                    average.append(0)
                    count.append(0)

                for j in range(0,len(histogram)):
                    number = j%period
                    bin[number] = bin[number] + histogram[j]
                    count[number] = count[number] + 1

                for k in range(0,len(bin)):
                    average[k] = bin[k]/count[k]


                for k in range(0,len(average)):
                    for j in range(k, len(average)):
                        final = compareWeek(average[k], average[j], final)

    # if len(histogram)>period2:
    #     if check != "Weekly":
    #         if check != "Monthly":
    #             bin2 = []
    #             average2 = []
    #             count2 = []
    #             for k in range(0,period2):
    #                 bin2.append(0)
    #                 average2.append(0)
    #                 count2.append(0)
    #
    #             for j in range(0, len(histogram)):
    #                 number = j % period2
    #                 bin2[number] = bin2[number] + histogram[j]
    #                 count2[number] = count2[number] + 1
    #
    #             for k in range(0, len(bin2)):
    #                 average2[k] = bin2[k] / count2[k]
    #
    #             for k in range(0, len(average2)):
    #                 for j in range(k, len(average2)):
    #                     final = compareMonth(average2[k], average2[j], final)


    #Smooth
    if checksmooth<10:
        if final != "Peaks":
            final = "Smooth"

    #Few values
    if percentage < thresholdFewValues:
        final = "Few Values"


    # Peaks
    if len(histogram)>lagPeaks:
        if countPeaks < thresholdPeaksNumber and countPeaks > lowerthresholdPeaksNumber:
            if final != "Weekly":
                if final != "Few Values" :
                    final = "Peaks"

    if len(histogram)>lagPeaks:
        if countPeaks2 < thresholdPeaksNumber and countPeaks2 > lowerthresholdPeaksNumber:
            if final != "Weekly":
                if final != "Few Values" :
                    if final != "Peaks":
                        final = "Peaks2"

    if len(histogram)>lagPeaks:
        if countPeaks3 < thresholdPeaksNumber and countPeaks3 > lowerthresholdPeaksNumber:
            if final != "Weekly":
                if final != "Few Values" :
                    if final != "Peaks":
                        if final != "Peaks2":
                            final = "Peaks3"

    if final == 0:
        final = "Random"

    print(percentage)

    if final == "Weekly":
        print(average)

    return final
