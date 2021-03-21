

choice = str(input("Would you like to proceed: "))

while choice == "yes":
  principle = float(input("Enter starting balance: $"))
  interestRate = float(input("Enter interest rate: "))
  annualInterest = 0
  e = principle
  print()
  print(format("YEAR",'5'), format("BEGINNING",'12'), format("ENDING",'11'))
  print(format("",'5'), format("BALANCE",'12'), format("BALANCE",'11'))
  def interestGain(principle, interestRate):
      annualInterest = principle * interestRate
      return annualInterest

  for count in range(1,6,1):
    a = count
    b = principle
    
    interestGain(principle, interestRate)
    annualInterest = interestGain(principle, interestRate)
    c = annualInterest
    
    principle = float(annualInterest + principle)
    d = principle
    
    print(format(a,'<5d'),"$",format(b,'<9.2f'),"  $",format(d,'<9.2f'))

  totalInterest = principle - e
  print()
  print("Total interest aquired: $",format(totalInterest, ',.2f'))
  
  choice = str(input("\nWould you like to start over? "))
  print("\n")
    
    
    
    



