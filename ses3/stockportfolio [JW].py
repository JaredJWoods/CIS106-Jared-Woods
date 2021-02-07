print("How many shares of CISQ do you own?")
shares = float(input())
print("You own ", shares, "of CISQ.")
print("What is the current market value of CISQ?")
cmv = float(input())
print("The current market value of CISQ is $", cmv,".")
portfolio = shares * cmv
print("Your portfolio value is: $", portfolio, ".")

