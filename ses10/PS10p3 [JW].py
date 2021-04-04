lastName = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller",
    "Wilson", "Moore", "Taylor"
]
#creates an array called lastNames which contains 10 names.
examScore = [88, 68, 87, 85, 72, 73, 94, 96, 83, 93]


#examScore list is parallel to lastName
def displayNames(lastName, examScore):
    for index in range(0, len(lastName)):
        print(
            format(str(index + 1), '>2') + ":\t " + str(lastName[index]) +
            "  \t" + str(examScore[index]) + "%")


#because the index starts at 0, 1 is added to the index so it
#represents the list count.
def displayReverse(lastName, examScore):
    lastName.reverse()
    examScore.reverse()
    #reverses the index of lastName
    for revIndex in range(0, len(lastName)):
        print(
            format(str(revIndex + 1), '>2') + ":\t " +
            str(lastName[revIndex]) + "  \t" + str(examScore[revIndex]) + "%")
    lastName.reverse()
    examScore.reverse()


    #reverts index back to normal
def average(examScore):
    total = 0
    for index in range(len(examScore)):
        total += examScore[index]
        average = (total / (index + 1))
    print(format("Class Mean:", "<14") + str(average) + "%")


def lowest(examScore):
    minimum = examScore[0]
    for index in range(1, len(examScore)):
        if minimum > examScore[index]:
            minimum = examScore[index]
            low = index
    return (minimum, low)


def highest(examScore):
    maximum = examScore[0]
    for index in range(1, len(examScore)):
        if maximum < examScore[index]:
            maximum = examScore[index]
            high = index
            #if the if statement does not run, this does not work
    return (maximum, high)
    

def main():
    print("----LAST NAME------")
    displayNames(lastName, examScore)
    print("\n----LAST FIRST-----")
    displayReverse(lastName, examScore)
    print("\n----AVERAGE SCORE--")
    average(examScore)
    print("\n----LOWEST SCORE---")
    minimum, low = lowest(examScore)
    print(format(str(lastName[low]), '<16') + str(minimum) + "%")
    print("\n----HIGHEST SCORE--")
    maximum, high = highest(examScore)
    print(format(str(lastName[high]), '<16') + str(maximum) + "%")
    highest(examScore)

main()
