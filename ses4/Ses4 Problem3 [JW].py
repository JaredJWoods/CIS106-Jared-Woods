print("$25 shipping fee waived for orders over $50")
print("Type the price of your book[s] followed by [ENTER].")
c=float(input())
print("The cost per book is: $",c)
print("How many books will you be ordering?")
q=int(input())
print("You are requesting:",q,"book[s].")
t=float(c*q)
print("Your subtotal comes to: $",t)
if t>50:
  print("You qualify for free shipping.")
  s=0
else:
  print("There is a $25 shipping fee.")
  s=25
print("SUBTOTAL:         $",t)
print("SHIPPING FEE:     $",s)
b=float(t+s)
print("TOTAL AMOUNT DUE: $", b)


