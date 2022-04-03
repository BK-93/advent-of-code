import csv

increaseCount = 0
currentSum = 0
lastSum = 0
lastNumber = 0
currentNumber = 0

with open('inputDay1.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)

    for row in datareader:
        lastNumber = currentNumber
        lastSum = currentSum
        print("Last sum: " + str(lastSum))
        currentNumber = int(row[0])
        currentSum = lastNumber + currentNumber
        print("Sum: " + str(lastNumber) + " + " + str(currentNumber) + " = " + str(currentSum))
        print("New sum: " + str(currentSum))
        print("Increase count: " + str(increaseCount))
        print("------------------")

        if currentSum > lastSum:
            increaseCount += 1

print(increaseCount - 1)
