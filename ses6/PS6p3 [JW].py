def cashRegister(gal):
  cost = float(gal) * 2.5
  return cost

def mpg(miles, gal):
  mpg = float(miles) / float(gal)
  return mpg

city = str(input("Enter destination city: "))
miles = float(input("Enter miles travelled: "))
gal = float(input("Enter gallons of gas used: "))

mpg = mpg(miles, gal)
cost = cashRegister(gal)

print("Destination City: ", city)
print("Miles travelled: ", miles)
print("Gallons used: ", gal)
print("Average MPG: ", mpg)
print("Cost of gas: $", cost)
