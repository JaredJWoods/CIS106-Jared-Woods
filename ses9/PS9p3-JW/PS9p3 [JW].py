def bonus(salary):
    bonus = float(salary) * float(0.10)
    return bonus


count = 0  # counter for the average
f = open("file1.txt", "r")
lastname = f.readline()
bonusPay = 0
totalBonus = 0
#I guess variables and functions do not like sharing a name?
while lastname != "":
    salary = f.readline()
    count = count + 1
    print("EMPLOYEE LAST NAME: ", lastname.strip())
    #I couldn't figure out what was causing a blank line printed.  strip helped, just not sure what caused it
    print("EMPLOYEE SALARY:     $", format(float(salary), '10,.2f'))
    bonusPay = bonus(salary)
    print("EMPLOYEE BONUS:      $", format(bonusPay, '10,.2f'))
    print()
    lastname = f.readline()
    totalBonus = totalBonus + bonusPay

f.close()
print()


print("AVERAGE BONUS:\t\t $", format(totalBonus, '10,.2f'))
