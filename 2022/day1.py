import csv

mostCalories = 0
elvesList = []
topThree = []
calorieCounter = 0

with open('input/input1.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)

    for row in datareader:
        if row:
            calorieCounter += int(row[0])

        else:
            elvesList.append(calorieCounter)
            calorieCounter = 0

    topThree = sorted(elvesList, reverse=True)[:3]
    mostCalories = sum(topThree)

print(mostCalories)
