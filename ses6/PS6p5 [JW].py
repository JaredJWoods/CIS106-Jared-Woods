def tuitionOwed(code, hours):
  if code == "I":
    tuition = float(250 * hours) 
  elif code == "O":
    tuition = float(550 * hours)
  else:
    print("ERROR!")
  
  return tuition

name = str(input("Enter student's last name: "))
code = str(input("Enter district code, I or O: "))
hours = float(input("Enter credit hours:  "))

tuition = tuitionOwed(code, hours)

print("STUDENT NAME: ", name)
print("TUITION COST: $", tuition)
