def examAverage(exam1, exam2):
  average = (exam1+exam2)/2
  return average

print("Would you like to check your exam average?")
choice = input("Type 'yes' or 'no': ")
print()

while choice == str("yes"):
  exam1 = float(input("Enter your score for the 1st exam: "))

  exam2 = float(input("Enter your score for the 2nd exam: "))
  average = examAverage(exam1, exam2)
  print("Your average score is:            ",average, "%")
  print()
  print("Would you like to check another average?")
  choice = input("Type 'yes' or 'no': ")
  print()
  print()

print()
print("Goodbye.")