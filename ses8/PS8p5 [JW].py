def incomeTax(gross):
  
  if gross >= 500001:
    rate = 0.30
    print("You are in the highest tax bracket with a 30% federal income tax rate.")
  elif gross >= 200000 and gross <= 500000:
    rate = 0.20
    print("You are in the middle tax bracket with a 20% federal income tax rate.")
  else:
    rate = 0.15
    print("You are in the lowest tax bracket with a 15% federal income tax rate.")

  taxOwed = float(gross * rate)

  return rate, taxOwed

#------------------program starts here-------------------
print("Would you like me to calculate your federal income tax?")
choice = str(input("Type 'yes' or 'no':        "))

while choice == "yes":
  print("Thank you for selecting yes.")
  gross = float(input("Please enter your gross income:   $"))
  print()
  print("You entered a gross income of $",gross)

  rate, taxOwed = incomeTax(gross)
  percent = int (rate*100)
  print("You have a tax rate of",percent,"%")
  print("The amount of tax you owe is: $",taxOwed)
  print()
  choice = input("Would you like to compute your income tax again? Enter 'yes' or 'no': ")

print("Thank you for using our income tax calculator.  Good bye.")

