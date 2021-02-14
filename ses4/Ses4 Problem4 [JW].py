print("Enter the name of your appliance.")
a=str(input())
print("You entered:",a)
print("Enter the cost of the appliance: $")
c=float(input())
print("APPLIANCE:",a)
print("COST: $",c)
if c>1000:
  w=float(c*0.01)
else:
  w=float(c*.05)
print("COST OF WARRANTEE: $",w)
t=float(c+w)
print("TOTAL WITH WARRANTEE: $",t)
