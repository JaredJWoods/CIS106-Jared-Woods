print("Please enter the price of the item you are purchasing:")
price = float(input())
print("Your item is: $",price,".")
print("How many items would you like to purchase?")
amount = float(input())
subtotal = price*amount
print("That amount comes to: $",subtotal,".")
discount = subtotal*.15
print("Your item is on sale for 15% off.  This saves you: $",discount,".")
total = subtotal - discount
print("This brings your new total to: $",total,".")
