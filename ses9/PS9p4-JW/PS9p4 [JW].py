#function to calculate extendedPrice
def extPrice(quantity, price):
  #declares to incoming variables as float
  extendedPrice = float(quantity) * float(price)
  return extendedPrice

#initializes variables
count = 0
totalEP = 0

#opens text file
f = open("order.txt",'r')
#places first line intpo item
item = f.readline()

print()
print("--------------------------------------------------------")
print("ITEM\t\t QUANTITY\t  PRICE\t\t\tEXTENDED PRICE")

while item != "":
  quantity = f.readline() #reads quantity in as a STRING
  price = f.readline()   #reads price in as a STRING
  
  extPrice(quantity,price)
  extendedPrice = extPrice(quantity,price)
  
  a = item.strip()
  b = int(quantity)
  c = float(price)
  d = float(extendedPrice)

  totalEP = extendedPrice + totalEP
  
  print(format(a,'12'),format(b,'<12'),'$',format(c,"<12,.2f"),'$',format(d,"<,.2f"))
  
  count = count + 1
  item = f.readline()


average = totalEP / count
print()
print("--------------------------------------------------------")
print("TOTAL EXTENDED PRICE      $",format(totalEP,'<10,.2f'))
print("TOTAL ORDERS              ",format(count,'>10d'))
print("AVERAGE PRICE PER ORDER.  $",format(average,'<10,.2f'))
print("--------------------------------------------------------")