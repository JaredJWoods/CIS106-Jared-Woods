def totalandDiscount():
  global discountAmount
  global total
  global subtotal
  subtotal = quantity * price
  discountAmount=(discount/100)*subtotal
  if discount != 0:
    total = subtotal - discountAmount
  else:
    total = subtotal
      
quantity=float(input("Enter quantity:         "))
price=   float(input("Enter price:           $"))
discount=float(input("Enter discount percent: "))

totalandDiscount()

print()
print("Subtotal:              ", subtotal)
print("Percent off:           ", discount,"%")
print("Discounted amount:   -$", discountAmount)
print("Discounted total:     $", total)
