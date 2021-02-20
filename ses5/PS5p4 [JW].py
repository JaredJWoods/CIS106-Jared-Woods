qty = int(input("How many tickets do you want to purchase? "))
if qty >= 25:
  price = 50
elif qty >= 10:
  price = 60
elif qty >= 5:
  price = 70
else:
  price = 75
total = int(qty * price)
print("Tickets:          ",qty)
print("Ticket Price:    $",price)
print("Total:           $",total)    
