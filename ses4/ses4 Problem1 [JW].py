print("Enter quantity of item:")
q = int(input())
print("You entered: ", q)
if q >= 1000:
    print("Unit price is: $3.00")
    pE = q * 3
else:
    print("Unit price is: $5.00")
    pE = q * 5
print("Extended price is: $", pE)
tax = float(pE*0.07)
print("Tax: $",float(tax))
# How do get rid of all the 00000000000?
total = float(pE + tax)
# how do I display currency 
print("Total is: $",total)
