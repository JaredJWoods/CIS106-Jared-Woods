
#------------------------CLASS_SETUP--------------------------
class Employee:
	
	bonus_rate = 0.0
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return 'NAME: {} {}'.format(self.first, self.last)

	def apply_rate(self):
		self.pay_total = int(self.pay * (self.bonus_rate + 1))

	def display_all(self):
		print(self.fullname())
		print('BASE PAY: \t$' + format(self.pay,',.2f'))
		self.apply_rate()
		print('BONUS PAY: \t$' + format(self.pay_total, ',.2f'))
		print()

#---------------------OBJECT_CREATION---------------------------
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)	

#-------------------------FUNCTIONS-----------------------------
def loop_stop():
	print('Would you like to change the bonus percent? ')
	loop = input("Enter [y] or [n]: ")
	return loop

def rate_input():	
	Employee.bonus_rate = float(input('\nEnter bonus rate as a decimal: '))
	print('\nCLASS BONUS RATE: \t\t' + str(Employee.bonus_rate * 100) + ' %')
	print('------------------------------')



#-----------------------PROGRAM_LOOP----------------------------
loop = loop_stop()

while loop == 'y':
	rate_input()
	emp_1.display_all()
	emp_2.display_all()
	loop = loop_stop()

print('\n-----END-----')
	



