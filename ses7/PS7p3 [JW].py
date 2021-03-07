def salesCalc():
  global commission
  global targetAmount
  target = float(sales * 0.05)
  targetAmount = float(target + sales)

  if sales > 100000:
    commission = sales * 0.10
  else:
    commission = target

print               ("                   Welcome!")
print               ("                    to the")
print               ("                  2021 Sales")
print               ("                    Report")
print()
print()
firstName= str(input("Enter first name:                      "))
lastName=  str(input("Enter last name:                       "))
sales =  float(input("Enter dollar amount sold:              $ "))
salesCalc()
print()
print(               "Salesperson:                          ", firstName, lastName)
print(               "Commission earned:                     $", commission)
print(               "Next year's target sales amount:       $", targetAmount)
