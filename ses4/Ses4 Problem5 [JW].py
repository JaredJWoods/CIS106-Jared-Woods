print("Type your last name and press [ENTER].")
name=str(input())
print("Enter your number of dependents.")
dependents=int(input())
print("Enter your gross income: $")
gross=int(input())
adjusted=float(gross-dependents*12000)
if adjusted>50000:
  tax=float(adjusted*0.2)
else:
  tax=float(adjusted*0.1)
if tax>0:
  pass
else: 
  tax=100
print("NAME:", name)
print("GROSS INCOME: $", gross)
print("DEPENDENTS:", dependents)
print("ADJUSTED GROSS INCOME: $", adjusted)
print("INCOME TAX: $", tax)