partno = int(input("Enter Part Number:"))
qty = int(input("Enter quantity to purchase:"))
if partno == 10 or partno == 55:
  unitcost = 1
elif partno == 99:
  unitcost = 2
elif partno == 70 or partno == 80:
  unitcost = 3
else:
  unitcost = 5
totalcost = float(qty * unitcost)
print("Part Number:          ", partno)
print("Cost per Unit:       $", unitcost)
print("Total Cost:          $", totalcost)

