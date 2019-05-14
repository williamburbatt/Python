# William Burbatt
# 5/8/2019
# Final Exam 
# ACSG-460
# Spring 2019
# Solve the following unsupervised learning problem:

# Apply the k-Means Clustering algorithm from sklearn (Links to an external site.)Links to an external site. to analyze the churn data set Preview the documentas presented in Slides 32-39 of Daniel LaRose's Hierarchical and K-Means Clustering, Chapter 10, Discovering Knowledge in Data. The slides are in one of your Pages.


# General INSTRUCTIONS:

# You must write a Python 3 program that solves the above problem
# You must comment your program at the top as I have shown you in class. Also do NOT forget to comment what you do within the body of your program..
# your program must use the tools and libraries we have used in class; they are described in Section 1.4 of the textbook by A. Muller & S. Guido.
# The k-Means algorithm is presented in Section 10.2.1 of the textbook by David L. Poole & Alan K. Mackworth
# (Artificial Intelligence,  2nd edition)  and in Section 3.5.1 of the textbook by A. Muller & S. Guido.
# NO COLLABORATION is ALLOWED: You will get zero if I find that you did not solve the exam on your own.


import matplotlib.pyplot as plt
import csv  # To read csv file
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd


# Normalizes data
def normalize_entry(entry, min, range):
    temp = float(entry) - float(min)
    result = float(temp) / float(range)
    return result


# finds minimum
def find_min(curr, prevMin):
    if float(curr) < float(prevMin):
        return curr
    return prevMin


# finds max
def find_max(curr, prevMin):
    if float(curr) > float(prevMin):
        return curr
    return prevMin


# finds averages of input
def findAverages(curr_data):
    averages = []
    accLen = 0
    vmMess = 0
    dayMins = 0
    eveMins = 0
    nightMins = 0
    intMins = 0
    custServCalls = 0
    for entry in curr_data:
        accLen += entry[2]
        vmMess += entry[3]
        dayMins += entry[4]
        eveMins += entry[5]
        nightMins += entry[6]
        intMins += entry[7]
        custServCalls += entry[8]

    averages.append(accLen / len(curr_data))
    averages.append(vmMess / len(curr_data))
    averages.append(dayMins / len(curr_data))
    averages.append(eveMins / len(curr_data))
    averages.append(nightMins / len(curr_data))
    averages.append(intMins / len(curr_data))
    averages.append(custServCalls / len(curr_data))
    return averages


# cluster chart
def create_cluster_chart(yes_val, no_val, title):
    values = [yes_val, no_val]
    colors = ['lightskyblue', 'lightcoral']
    labels = ["yes", "no"]
    patches, texts = plt.pie(values, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title(title)
    plt.axis('equal')
    plt.tight_layout()
    return plt


# churn cluster chart
def create_churn_chart(yes_val, no_val, title):
    values = [yes_val, no_val]
    colors = ['lightskyblue', 'lightcoral']
    labels = ["true", "false"]
    patches, texts = plt.pie(values, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title(title)
    plt.axis('equal')
    plt.tight_layout()
    return plt


# calculate churn for specific data
def calc_churn(data_set, churn_set):
    entry_count = 0
    churn_yes_count = 0
    churn_no_count = 0
    for entry in data_set:
        # yes int plan
        if entry[0] == 1:
            if churn_set[entry_count] == 1:
                churn_yes_count += 1
        else:
            if churn_set[entry_count] == 1:
                churn_no_count += 1
        entry_count += 1

    return [churn_yes_count, churn_no_count]


# calc churn for voicemail
def calc_churn_vm(data_set, churn_set):
    entry_count = 0
    churn_yes_count = 0
    churn_no_count = 0
    for entry in data_set:
        # yes vm plan
        if entry[1] == 1:
            if churn_set[entry_count] == 1:
                churn_yes_count += 1
        else:
            if churn_set[entry_count] == 1:
                churn_no_count += 1
        entry_count += 1

    return [churn_yes_count, churn_no_count]


# main method reads in data
def kmeans_churn():
    dataSet = []
    total_churn = []
    file_name = "churn.txt"
    # placeholders
    minAccLen = 0
    maxAccLen = 0
    minVMMess = 0
    maxVMMess = 0
    minDayMin = 0
    maxDayMin = 0
    minEvMin = 0
    maxEvMin = 0
    minNightMin = 0
    maxNightMin = 0
    minintMin = 0
    maxintMin = 0
    minCusSerCall = 0
    maxCusSerCall = 0
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        total = 0
        for r in csv_reader:
            if total == 0:
                print(r)
            # first data becomes max and min for all data
            elif total == 1:
                temp = []

                internationalPlan = r[4]
                if internationalPlan == "no":
                    temp.append("0")
                else:
                    temp.append("1")

                voiceMailPlan = r[5]
                if voiceMailPlan == "no":
                    temp.append("0")
                else:
                    temp.append("1")

                accountLength = r[1]
                temp.append(accountLength)
                minAccLen = accountLength
                maxAccLen = accountLength

                voiceMailMessages = r[6]
                temp.append(voiceMailMessages)
                minVMMess = voiceMailMessages
                maxVMMess = voiceMailMessages

                dayMinutes = r[7]
                temp.append(dayMinutes)
                minDayMin = dayMinutes
                maxDayMin = dayMinutes

                eveningMinutes = r[10]
                temp.append(eveningMinutes)
                minEvMin = eveningMinutes
                maxEvMin = eveningMinutes

                nightMinutes = r[13]
                temp.append(nightMinutes)
                minNightMin = nightMinutes
                maxNightMin = nightMinutes

                internationalMinutes = r[16]
                temp.append(internationalMinutes)
                minintMin = internationalMinutes
                maxintMin = internationalMinutes

                customerServiceCalls = r[19]
                temp.append(customerServiceCalls)
                minCusSerCall = customerServiceCalls
                maxCusSerCall = customerServiceCalls

                churn = r[20]
                if churn == 'False.':
                    total_churn.append(0)
                else:
                    total_churn.append(1)

                print(temp)
                dataSet.append(temp)

            else:
                temp = []

                internationalPlan = r[4]
                if internationalPlan == "no":
                    temp.append("0")
                else:
                    temp.append("1")

                voiceMailPlan = r[5]
                if voiceMailPlan == "no":
                    temp.append("0")
                else:
                    temp.append("1")

                accountLength = r[1]
                temp.append(accountLength)
                minAccLen = find_min(accountLength, minAccLen)
                maxAccLen = find_max(accountLength, maxAccLen)

                voiceMailMessages = r[6]
                temp.append(voiceMailMessages)
                minVMMess = find_min(voiceMailMessages, minVMMess)
                maxVMMess = find_max(voiceMailMessages, minVMMess)

                dayMinutes = r[7]
                temp.append(dayMinutes)
                minDayMin = find_min(dayMinutes, minDayMin)
                maxDayMin = find_max(dayMinutes, maxDayMin)

                eveningMinutes = r[10]
                temp.append(eveningMinutes)
                minEvMin = find_min(eveningMinutes, minEvMin)
                maxEvMin = find_max(eveningMinutes, maxEvMin)

                nightMinutes = r[13]
                temp.append(nightMinutes)

                minNightMin = find_min(nightMinutes, minNightMin)
                maxNightMin = find_max(nightMinutes, maxNightMin)

                internationalMinutes = r[16]
                temp.append(internationalMinutes)
                minintMin = find_min(internationalMinutes, minintMin)
                maxintMin = find_max(internationalMinutes, maxintMin)

                customerServiceCalls = r[19]
                temp.append(customerServiceCalls)
                minCusSerCall = find_min(customerServiceCalls, minCusSerCall)
                maxCusSerCall = find_max(customerServiceCalls, maxCusSerCall)

                churn = r[20]
                if (churn == 'False.'):
                    total_churn.append(0)
                else:
                    total_churn.append(1)

                dataSet.append(temp)
            total += 1
    # find ranges
    alRange = float(maxAccLen) - float(minAccLen)
    print("alRange:", alRange)
    vmmRange = float(maxVMMess) - float(minVMMess)
    print("vmRange:", vmmRange)
    dayMinRange = float(maxDayMin) - float(minDayMin)
    print("dayMinRange:", dayMinRange)
    evMinRange = float(maxEvMin) - float(minEvMin)
    print("evMinRange:", evMinRange)
    nightMinRange = float(maxNightMin) - float(minNightMin)
    print("nightMinRange:", nightMinRange)
    intMinRange = float(maxintMin) - float(minintMin)
    print("intMinRange:", intMinRange)
    custServCallRange = float(maxCusSerCall) - float(minCusSerCall)
    print("custServCallsRange:", custServCallRange)

    print(dataSet)
    normalizedData = []
    # normalize all data
    for entry in dataSet:
        tempEntry = [entry[0], entry[1], normalize_entry(entry[2], minAccLen, alRange),
                     normalize_entry(entry[3], minVMMess, vmmRange),
                     normalize_entry(entry[4], minDayMin, dayMinRange), normalize_entry(entry[5], minEvMin, evMinRange),
                     normalize_entry(entry[6], minNightMin, nightMinRange),
                     normalize_entry(entry[7], minintMin, intMinRange),
                     normalize_entry(entry[8], minCusSerCall, custServCallRange)]
        normalizedData.append(tempEntry)
    print("Normalized Data:")
    print(normalizedData)
    print("Begin kmeans:")
    # fit into clusters
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(normalizedData)
    data_prediction = (kmeans.predict(normalizedData))
    print(data_prediction)
    labels = ["0", "1", "2"]
    unique, counts = np.unique(data_prediction, return_counts=True)
    testDict = dict(zip(unique, counts))
    print("Clusterings:", testDict)
    zero_count = testDict[0]
    one_count = testDict[1]
    two_count = testDict[2]
    values = [zero_count, one_count, two_count]
    colors = ['yellowgreen', 'lightskyblue', 'lightcoral']
    patches, texts = plt.pie(values, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title('Number in each cluster')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    zero_data = []
    zero_churn_data = []
    one_data = []
    one_churn_data = []
    two_data = []
    two_churn_data = []
    entry_count = 0

    # entries for int plan

    int_plan_yes = 0
    int_plan_zero_yes = 0
    int_plan_one_yes = 0
    int_plan_two_yes = 0

    # entries for vmplan

    vm_plan_yes = 0
    vm_plan_zero_yes = 0
    vm_plan_one_yes = 0
    vm_plan_two_yes = 0

    # data for churn

    yes_int_churn = 0
    no_int_churn = 0
    yes_vm_churn = 0
    no_vm_churn = 0

    for entry in data_prediction:

        temp = normalizedData[entry_count]
        curr_churn = total_churn[entry_count]

        # int plan true
        if temp[0] == '1':
            int_plan_yes += 1
            if entry == 0:
                int_plan_zero_yes += 1
            if entry == 1:
                int_plan_one_yes += 1
            if entry == 2:
                int_plan_two_yes += 1
            if curr_churn == 1:
                yes_int_churn += 1
        else:
            if curr_churn == 1:
                no_int_churn += 1

        # vm plan true
        if temp[1] == '1':
            vm_plan_yes += 1
            if entry == 0:
                vm_plan_zero_yes += 1
            if entry == 1:
                vm_plan_one_yes += 1
            if entry == 2:
                vm_plan_two_yes += 1
            if curr_churn == 1:
                yes_vm_churn += 1
        else:
            if curr_churn == 1:
                no_vm_churn += 1

        # count each cluster
        if entry == 0:
            zero_data.append(temp)
            zero_churn_data.append(curr_churn)
        if entry == 1:
            one_data.append(temp)
            one_churn_data.append(curr_churn)
        if entry == 2:
            two_data.append(temp)
            two_churn_data.append(curr_churn)

        entry_count += 1

    print(int_plan_yes)
    print(vm_plan_yes)
    int_plan_no = total - int_plan_yes
    int_plan_zero_no = len(zero_data) - int_plan_zero_yes
    int_plan_one_no = len(one_data) - int_plan_one_yes
    int_plan_two_no = len(two_data) - int_plan_two_yes

    vm_plan_no = total - vm_plan_yes
    vm_plan_zero_no = len(zero_data) - vm_plan_zero_yes
    vm_plan_one_no = len(one_data) - vm_plan_one_yes
    vm_plan_two_no = len(two_data) - vm_plan_two_yes

    # INT PLAN CHARTS

    # chart for all clusters int plan

    all_cluster_int_plt = create_cluster_chart(int_plan_yes, int_plan_no, "Int Plan All Clusters")
    all_cluster_int_plt.show()

    # chart for cluster one
    cluster_one_int_plan = create_cluster_chart(int_plan_zero_yes, int_plan_zero_no, 'Int Plan Cluster 1')
    cluster_one_int_plan.show()

    # chart for cluster two
    cluster_two_int_plan = create_cluster_chart(int_plan_one_yes, int_plan_one_no, 'Int Plan Cluster 2')
    cluster_two_int_plan.show()

    # chart for cluster three
    cluster_three_int_plan = create_cluster_chart(int_plan_two_yes, int_plan_two_no, 'Int Plan Cluster 3')
    cluster_three_int_plan.show()

    # VM PLAN CHARTS

    # chart for all clusters vm plan

    all_cluster_vm_plt = create_cluster_chart(vm_plan_yes, vm_plan_no, "VM Plan All Clusters")
    all_cluster_vm_plt.show()

    # chart for cluster one
    cluster_one_vm_plan = create_cluster_chart(vm_plan_zero_yes, vm_plan_zero_no, 'VM Plan Cluster 1')
    cluster_one_vm_plan.show()

    # chart for cluster two
    cluster_two_vm_plan = create_cluster_chart(vm_plan_one_yes, vm_plan_one_no, 'VM Plan Cluster 2')
    cluster_two_vm_plan.show()

    # chart for cluster three
    cluster_three_vm_plan = create_cluster_chart(vm_plan_two_yes, vm_plan_two_no, 'VM Plan Cluster 3')
    cluster_three_vm_plan.show()

    zero_averages = (findAverages(zero_data))
    one_averages = (findAverages(one_data))
    two_averages = (findAverages(two_data))
    # Dictonary containing means data
    data = {'Clustering': ['0', '1', '2'],
            'Freq': [zero_count, one_count, two_count],
            'AcctLen_m': [zero_averages[0], one_averages[0], two_averages[0]],
            'VMAILMessage': [zero_averages[1], one_averages[1], two_averages[1]],
            'DayMins_mm': [zero_averages[2], one_averages[2], two_averages[2]],
            'EveMins_mm': [zero_averages[3], one_averages[3], two_averages[3]],
            'NightMins_mm': [zero_averages[4], one_averages[4], two_averages[4]],
            'IntMins_mm': [zero_averages[5], one_averages[5], two_averages[5]],
            'CustServCalls': [zero_averages[6], one_averages[6], two_averages[6]]
            }

    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)
    print(df)

    # begin churn charts
    print(total_churn)

    # Churn for all clusters with International Plan
    yes_int_churn_diff = int_plan_yes - yes_int_churn
    churn_chart_yes_int_plan_all_cluster = create_churn_chart(yes_int_churn, yes_int_churn_diff,
                                                              "Yes Int Plan Churn All Clusters")
    churn_chart_yes_int_plan_all_cluster.show()

    # Churn for all clusters without international plan
    no_int_churn_diff = int_plan_no - no_int_churn
    churn_chart_no_int_plan_all_cluster = create_churn_chart(no_int_churn, no_int_churn_diff,
                                                             "No Int Plan Churn All Clusters")
    churn_chart_no_int_plan_all_cluster.show()

    # Start cluster 0

    churn_int_plan_cluster_zero = calc_churn(zero_data, zero_churn_data)

    yes_int_churn_zero_diff = int_plan_zero_yes - churn_int_plan_cluster_zero[0]

    # chart for cluster zero
    cluster_zero_int_plan_churn = create_churn_chart(churn_int_plan_cluster_zero[0], yes_int_churn_zero_diff,
                                                     'Int Plan Churn Cluster 1')
    cluster_zero_int_plan_churn.show()

    no_int_churn_zero_diff = int_plan_zero_no - churn_int_plan_cluster_zero[1]
    # chart for cluster zero
    cluster_zero_no_int_plan_churn = create_churn_chart(churn_int_plan_cluster_zero[1], no_int_churn_zero_diff,
                                                        'No Int Plan Churn Cluster 1')
    cluster_zero_no_int_plan_churn.show()

    # Start cluster 1

    churn_int_plan_cluster_one = calc_churn(one_data, one_churn_data)

    yes_int_churn_one_diff = int_plan_zero_yes - churn_int_plan_cluster_one[0]

    # chart for cluster one
    cluster_one_int_plan_churn = create_churn_chart(churn_int_plan_cluster_one[0], yes_int_churn_one_diff,
                                                    'Int Plan Churn Cluster 2')
    cluster_one_int_plan_churn.show()

    no_int_churn_one_diff = int_plan_zero_no - churn_int_plan_cluster_one[1]
    # chart for cluster one
    cluster_one_no_int_plan_churn = create_churn_chart(churn_int_plan_cluster_one[1], no_int_churn_one_diff,
                                                       'No Int Plan Churn Cluster 2')
    cluster_one_no_int_plan_churn.show()

    # Start cluster 2

    churn_int_plan_cluster_two = calc_churn(two_data, two_churn_data)

    yes_int_churn_two_diff = int_plan_one_yes - churn_int_plan_cluster_two[0]

    # chart for cluster two
    cluster_two_int_plan_churn = create_churn_chart(churn_int_plan_cluster_two[0], yes_int_churn_two_diff,
                                                    'Int Plan Churn Cluster 3')
    cluster_two_int_plan_churn.show()

    no_int_churn_two_diff = int_plan_one_no - churn_int_plan_cluster_two[1]
    # chart for cluster two
    cluster_two_no_int_plan_churn = create_churn_chart(churn_int_plan_cluster_two[1], no_int_churn_two_diff,
                                                       'No Int Plan Churn Cluster 3')
    cluster_two_no_int_plan_churn.show()

    # Churn charts for VM Plan

    # Churn for all clusters with VM Plan
    yes_vm_churn_diff = vm_plan_yes - yes_vm_churn
    churn_chart_yes_vm_plan_all_cluster = create_churn_chart(yes_vm_churn, yes_vm_churn_diff,
                                                             "Yes vm Plan Churn All Clusters")
    churn_chart_yes_vm_plan_all_cluster.show()

    # Churn for all clusters without VM plan
    no_vm_churn_diff = vm_plan_no - no_vm_churn
    churn_chart_no_vm_plan_all_cluster = create_churn_chart(no_vm_churn, no_vm_churn_diff,
                                                            "No vm Plan Churn All Clusters")
    churn_chart_no_vm_plan_all_cluster.show()

    # Start cluster 0

    churn_vm_plan_cluster_zero = calc_churn_vm(zero_data, zero_churn_data)

    yes_vm_churn_zero_diff = vm_plan_zero_yes - churn_vm_plan_cluster_zero[0]

    # chart for cluster zero
    cluster_zero_vm_plan_churn = create_churn_chart(churn_vm_plan_cluster_zero[0], yes_vm_churn_zero_diff,
                                                    'vm Plan Churn Cluster 1')
    cluster_zero_vm_plan_churn.show()

    no_vm_churn_zero_diff = vm_plan_zero_no - churn_vm_plan_cluster_zero[1]
    # chart for cluster zero
    cluster_zero_no_vm_plan_churn = create_churn_chart(churn_vm_plan_cluster_zero[1], no_vm_churn_zero_diff,
                                                       'No vm Plan Churn Cluster 1')
    cluster_zero_no_vm_plan_churn.show()

    # Start cluster 1

    churn_vm_plan_cluster_one = calc_churn_vm(one_data, one_churn_data)

    yes_vm_churn_one_diff = vm_plan_zero_yes - churn_vm_plan_cluster_one[0]

    # chart for cluster one
    cluster_one_vm_plan_churn = create_churn_chart(churn_vm_plan_cluster_one[0], yes_vm_churn_one_diff,
                                                   'vm Plan Churn Cluster 2')
    cluster_one_vm_plan_churn.show()

    no_vm_churn_one_diff = vm_plan_zero_no - churn_vm_plan_cluster_one[1]
    # chart for cluster one
    cluster_one_no_vm_plan_churn = create_churn_chart(churn_vm_plan_cluster_one[1], no_vm_churn_one_diff,
                                                      'No vm Plan Churn Cluster 2')
    cluster_one_no_vm_plan_churn.show()

    # Start cluster 2

    churn_vm_plan_cluster_two = calc_churn_vm(two_data, two_churn_data)

    yes_vm_churn_two_diff = vm_plan_one_yes - churn_vm_plan_cluster_two[0]

    # chart for cluster two
    cluster_two_vm_plan_churn = create_churn_chart(churn_vm_plan_cluster_two[0], yes_vm_churn_two_diff,
                                                   'vm Plan Churn Cluster 3')
    cluster_two_vm_plan_churn.show()

    no_vm_churn_two_diff = vm_plan_one_no - churn_vm_plan_cluster_two[1]
    # chart for cluster two
    cluster_two_no_vm_plan_churn = create_churn_chart(churn_vm_plan_cluster_two[1], no_vm_churn_two_diff,
                                                      'No vm Plan Churn Cluster 3')
    cluster_two_no_vm_plan_churn.show()


kmeans_churn()
