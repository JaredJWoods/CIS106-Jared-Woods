def grossPay(hours, rate):
  if hours >= 40:
    OT = hours - 40
    base = 40 * rate
    OTpay = OT * rate * 1.5
    pay = OTpay + base
  else:
    pay = hours * rate

  return pay

def payRate(job):
  if job == "L":
    rate = 25
  elif job == "A":
    rate = 35
  elif job == "J":
    rate = 50
  else:
    print("ERROR!")

  return rate

name = str(input("Enter your last name: "))
job = str(input("Enter JOB CODE: L, A, or J. "))
hours = float(input("Enter hours worked: "))

rate = payRate(job)
pay = grossPay(hours, rate)

print()
print("NAME: ", name)
print("JOB CODE: ", job)
print("HOURS WORKED: ", hours)
print("PAY RATE: $",rate,"hour")
print("GROSS PAY: $",pay)