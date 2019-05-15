import csv  # To read csv file
from sklearn.neighbors import NearestNeighbors

# William Burbatt
# 4/30/2019
# Final Report
# ACSG-460
# Spring 2019


stats = []
players = []
age = ""
status = ""
income = ""
file_name = "players2.csv"

# This code opens the csv file and reads each record skipping empty rows.
print("Loading player data....")
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    total = 0
    for r in csv_reader:
        if r[0] == "Name":
            print(r)
        else:
            print(r)
            players.append(r[0])
            currList = [r[2]]
            for i in range(3, 22):
                currList.append(r[i])
            print(currList)
            stats.append(currList)
            total += 1

print("Total players:", total)
print(players)


def predictive_analysis(indexNumber):
    knn = NearestNeighbors(n_neighbors=10)

    knn.fit(stats)  # fit our sample data to to the knn function.
    target = []  # holder value for targeted value.
    print("Target: ", players[indexNumber], "-------------------------------")

    target.append(stats[indexNumber])

    print("These players are most similar to the target player:")

    solution = knn.kneighbors(
        target)  # using the kneighbors function we can get our three closest neighbors for this dataset.

    solutionDistances = solution[0][0]
    solutionPoints = solution[1][0]

    for x in range(10):
        print("Name ", players[solutionPoints[x]], " has a distance of ", solutionDistances[x])
    print("------------------------------------------------")


from tkinter import Tk, Label, Button, StringVar


class BaseballGUI:
    LABEL_TEXT = players

    def __init__(self, master):
        self.master = master
        master.title("Predictive Analysis")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.config(font=("Courier 24 bold"))
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack(pady=50)
        self.confirm_button = Button(master, text="Analyze", command=self.fire)
        self.confirm_button.pack(padx=300, pady=5)
        self.confirm_button.config(width=20, height=3, font=("Courier", 12))
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(pady=5)
        self.close_button.config(width=20, height=3, font=("Courier", 12))

    def fire(self):
        predictive_analysis(self.label_index)

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT)  # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])


root = Tk()
my_gui = BaseballGUI(root)
root.mainloop()
