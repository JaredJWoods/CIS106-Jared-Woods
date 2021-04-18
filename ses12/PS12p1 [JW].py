class employee:

	bonusRate = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def applyRate(self):
		self.pay = int(self.pay * employee.bonusRate)


emp1 = employee('Corey', 'Schafer', 50000)
emp2 = employee('Test', 'User', 60000)	

# EMP = [emp1,emp2] <------ I wanted an array for this


#-------------------------------------------
print('Would you like to change the bonus percent? ')
loop = input("Enter [y] or [n]: ")
bonusPercent = 0.0
bonusRate = float((bonusPercent/100)+1)


while loop == 'y':
	
	bonusPercent = float(input("\nEnter bonus as a percent: "))
	

	print('\nClass Bonus Rate: \t\t' + str(bonusPercent) + ' %')
	print('------------------------------')
	print(str(emp1.fullname) + 'Base Pay: \t$' + str(emp1.pay))
	emp1.applyRate()
	print('Employee 1 Bonus Pay: \t$' + str(emp1.pay))
	print('\nEmployee 2 Base Pay: \t$' + str(emp2.pay))
	emp2.applyRate()
	print('Employee 2 Bonus Pay: \t$' + str(emp2.pay))
	print("\nWould you like to change the bonus percent?")

	loop = input("Enter [y] or [n]: ")
	






