def averageTotal():
  global average
  global totalPoints
  totalPoints = (exam1 + exam2 + exam3)
  average = (totalPoints/3)

name =  str(input("Enter student's last name:            "))
print()
exam1 = int(input("Enter your score for the first exam:  "))
exam2 = int(input("Enter your score for the second exam: "))
exam3 = int(input("Enter your score for the third exam:  "))

averageTotal()
print()
print("Last name:            ",name)
print("Total points scored:  ",totalPoints,"/300 points")
print("Exam average:         ",average,"%")


