import csv

increaseCount = 0
currentNumber = 0
lastNumber = 0

with open('inputDay1.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        lastNumber = currentNumber
        print("Lastnumber: " + str(lastNumber))
        currentNumber = int(row[0])
        print("Currentnumber: " + str(currentNumber))
        print("------------------")

        if currentNumber > lastNumber:
            increaseCount += 1

print(increaseCount - 1)
