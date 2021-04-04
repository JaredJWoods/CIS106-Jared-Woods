lastName = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller",
    "Wilson", "Moore", "Taylor"
]
#creates an array called lastNames which contains 10 names.

examScore = [97, 68, 87, 85, 78, 73, 94, 96, 83, 97]
#examScore list is parallel to lastName


def displayNames(lastName, examScore): 
    for index in range(0, len(lastName)): 
        print(format(str(index + 1),'>2') + ":\t " + str(lastName[index]) + "  \t" + str(examScore[index]) + "%")
#because the index starts at 0, 1 is added to the index so it
#represents the list count.

def displayReverse(lastName, examScore):
    lastName.reverse() 
    examScore.reverse()
    #reverses the index of lastName
    for revIndex in range(0, len(lastName)):
        print(format(str(revIndex + 1),'>2') + ":\t " + str(lastName[revIndex]) + "  \t" + str(examScore[revIndex]) + "%")
    lastName.reverse()
    #reverts index back to normal

print("-----LAST NAME-----")
displayNames(lastName, examScore)
print("\n")
print("----LAST FIRST-----")
displayReverse(lastName, examScore)
