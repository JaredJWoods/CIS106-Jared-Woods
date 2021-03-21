no1 = 1
no2 = 1
no3 = 0

print("The Golden Ratio\n")

for count in range(1,21,1):
  print(no2)
  no3 = no1 + no2
  no1 = no2
  no2 = no3
  
