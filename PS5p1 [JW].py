qty = int(input("Enter Widgit Quantity: "))
if qty > 10000:
  extprice = float(qty*10)
elif qty >= 5000 and qty <= 10000:
  extprice = float(qty*20)
else:
  extprice = float(qty*30)
tax = float(extprice*.07)
total = float(tax+extprice)
print("Extended Price:      $", extprice)
print("Tax Amount:          $", tax)
print("Total:               $", total)