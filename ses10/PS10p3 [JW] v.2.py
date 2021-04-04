name = [
    "SMITH", "JOHNSON", "WILLIAMS", "JONES", "BROWN", "DAVIS", "MILLER",
    "WILSON", "MOORE", "TAYLOR"
]
score = [88, 68, 87, 85, 72, 73, 94, 96, 83, 93]


def display(name, score):
    print("----------------------------")
    total = 0
    low = 999
    high = 0

    for index in range(0, len(name)):
        print(
            format(str(index + 1), '<2') + " " +
            format(str(name[index]), '<10') + "\t\t " +
            format(score[index], '.2f') + " %")
        total += score[index]

        if score[index] < low:
            low = score[index]
            lowName = name[index]

        if score[index] > high:
            high = score[index]
            highName = name[index]

    average = total / len(name)

    print("----------------------------")
    print(format("Average Score:", '<21') + format(average, '.2f') + " %")
    print("----------------------------")
    print(format("Lowest Score:", '<21') + format(low, '.2f') + " %")
    print("\t\t\t\t\t " + lowName)
    print("----------------------------")
    print(format("Highest Score:", '<21') + format(high, '.2f') + " %")
    print("\t\t\t\t\t " + highName)
    print("----------------------------")


display(name, score)
