def compuTotal():
  global total
  global tax
  global subtotal
  subtotal = quantity * price
  tax = subtotal * float(0.07)
  total = subtotal + tax

quantity = float(input("Enter quantity:     "))
price =    float(input("Enter price:      $ "))  

compuTotal()
print()
print                 ("Your subtotal is: $", subtotal)
print                 ("7% sales tax is:  $", tax)
print                 ("Total incl. tax:  $", total)           