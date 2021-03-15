#This first function calculates everything
def cashRegister(quantity, price):
  extendedPrice = float(quantity) * float(price)

  if extendedPrice >= 10000.01:
    discount = float (extendedPrice * 0.10)
    rate = 10
  elif extendedPrice >= 5000.01:
    discount = float (extendedPrice * 0.05)
    rate = 5
  else:
    discount = float (extendedPrice * 0.02)
    rate = 2
  discountedPrice = float(extendedPrice - discount)
  tax = float(discountedPrice * 0.07)
  total = float(discountedPrice + tax)
  return extendedPrice, discount,discountedPrice,tax,rate, total
#------------------PROGRAM BEGINS----------------------
print("Welcome to Max and Oliver's Shop.")
choice = input("  Do you think you have enough money to buy something? ")

while choice == str("yes"):
  item = input("What are you buying? ")
  quantity = (input("   How many of those can you afford? "))
  price = float(input("What are you gonna give me for each one? $"))
  print()
  extendedPrice,discount,discountedPrice,tax,rate,total = cashRegister(quantity,price)

  print("You think you are going to get",quantity,item,"'s for $",price,"each!!")
  print("   There is no way you have $",extendedPrice)
  print()
  print("I'll bring your total down",rate,"%")
  print("That removes $",discount,"from the total.")
  print("Then I have to add 7% sales tax, which adds $",tax)
  print("That comes to a grand total of...           $",total)
  print()
  choice = input("Do you want to place another order? ")

print()
print("I didn't think so.  Come back when you have money.")






