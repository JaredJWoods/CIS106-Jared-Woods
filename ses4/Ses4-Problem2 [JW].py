print("Press [1] followed by [ENTER] to select Item A.")
print("Press [2] followed by [ENTER] to select Item B.")
item = int(input())
if item == 1:
  print("You selected Item A.")
  print("Unit price is: $10 per unit.")
  u=10
else:
  if item == 2:
    print("You selected Item B.")
    print("Unit price is: $5 per unit")
    u=5
  else:
    print("Your selection is INVALID.")
    print("Unit price is: $0 per unit")
    u=0
print("How many units are you purchasing?")
q = int(input())
pE=q*u
print("The price for:",q,"units is: $",pE,".")
