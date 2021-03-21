def tuitionCalc(credits):
  tuition = float(credits) * float(250.00)
  return tuition

print("STUDENT NAME\tCREDITS\t\t TUITION") 
count = 0
print("---------------------------------------")
tuitionSum = 0
f = open("roster.txt",'r')
lastname = f.readline()

while lastname != "":
  
  credits = f.readline()
  
  tuitionCalc(credits)
  tuition = tuitionCalc(credits)
  tuitionSum = tuition + tuitionSum
  
  a = format(lastname.strip(),'15')
  b = format(int(credits),'<12')
  c = format(float(tuition),'<8,.2f')

  print(a,b,"$",c)

  count = count + 1
  lastname = f.readline()

print()
print("---------------------------------------")
print("TOTAL NUMBER OF STUDENTS:\t\t\t",count)
print("TOTAL TUITION:\t\t\t\t$",format(tuitionSum,',.2f')) 
print("---------------------------------------") 