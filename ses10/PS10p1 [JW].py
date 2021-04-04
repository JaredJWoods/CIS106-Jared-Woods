lastName = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller",
    "Wilson", "Moore", "Taylor"
]

examScore = [97, 68, 87, 85, 78, 73, 94, 96, 83, 97]


def displayNames(lastName):
    for index in range(0, len(lastName)):
        print(str(index + 1) + "-" + str(lastName[index]))


def displayReverse(lastName):
    lastName.reverse()
    for revIndex in range(0, len(lastName)):
        print(str(revIndex + 1) + "-" + str(lastName[revIndex]))

print("---LAST NAME---")
displayNames(lastName)
print("\n")
print("---LAST FIRST---")
displayReverse(lastName)
