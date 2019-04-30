import csv  # To read csv file
from sklearn.neighbors import NearestNeighbors

# William Burbatt
# 3/27/2019
# Midterm Exam
# ACSG-460
# Spring 2019

# Solve the following Machine Learning problem:
# Using the data in the attached table midterm_SP2019.csvPreview the document, find the k-nearest neighbors for
# record #10 using k = 3
# INSTRUCTIONS:
# You must write a Python 3 program that solves the above problem You must comment your program at the top of your
# program as I have shown you in class. Also do NOT forget to comment what you do within the body of your program..
# your program must use the tools and libraries we have used in class; they are described in Section 1.4 of the
# textbook by A. Muller & S. Guido. NO COLLABORATION is ALLOWED: You will get zero if I find that you did not solve
# the exam on your own. You are NOT allowed to make manually any changes to the above csv file
# howToReadCSVfile.pyPreview the document shows you how to read the above csv file
# ==> Submit the py file that contains your solution and the csv file above zipped in the folder
# firstNameLastName_Midterm_ACSG460.zip
# ==> In your py file, in the comments at the top of your file list the 3-nearest neighbors of record #10.
#
# These points are the three closest neighbors to record #10
# ID  10  has a distance of  0.0
# ID  6  has a distance of  2125.6117222108037
# ID  3  has a distance of  7333.098526543875
#
#

samples = []
age = ""
status = ""
income = ""
file_name = "midterm_SP2019.csv"

# This code opens the csv file and reads each record skipping empty rows.
with open(file_name) as csv_file:
    mdterm_Reader = csv.reader(csv_file, delimiter=",")
    row_count = 0
    for r in mdterm_Reader:
        if r:  # this skips empty records.
            print(r)
            age = r[1]  # we only need age status and amount for our datasets.
            status = r[2]
            amount = r[3]
            currList = [age]
            if status == " Single":  # need to set integer values for single, married, or other.
                currList.append('0')
            else:
                if status == " Married":
                    currList.append('1')
                else:
                    currList.append('2')
            currList.append(amount)
            samples.append(currList)  # append our sample data with each record.
            row_count = row_count + 1

print("row count", row_count)
print("samples: ", samples)

knn = NearestNeighbors(n_neighbors=3)

knn.fit(samples)  # fit our sample data to to the knn function.
target = []  # holder value for targeted value.
print("target: ", samples[9])

target.append(samples[9])

print("These values are the closest to the target:")

solution = knn.kneighbors(
    target)  # using the kneighbors function we can get our three closest neighbors for this dataset.

solutionDistances = solution[0][0]
solutionPoints = solution[1][0]

for x in range(3):
    print("ID ", solutionPoints[x] + 1, " has a distance of ", solutionDistances[x])
