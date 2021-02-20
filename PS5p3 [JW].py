principle = float(input("Input Principle Amount: $"))
years = int(input("Enter years until maturity:"))
if principle > 100000 and years == 5:
  rate = 6
elif principle >= 50000 and years == 10:
  rate = 5
elif principle >= 50000 and years == 5:
  rate = 4
else:
  rate = 2
interest = (principle * rate/100)
print("Principle Amount:          $", principle)
print("Interest Rate:              ",rate,"%")
print("First Year Interest:       $",interest)