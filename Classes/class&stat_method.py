print("........................egular/class & static methods....................................") 
# Regular & Class methods automatically take the instence as the first argument
'''Regular method authomatically take in the instance as the first argument and how we change it, instead
of it automatically take the class as the argument. to change regular method into class method as easy as
using 'decorators' as (classmethod)''' 

# 1. Regular method automatically parse the instance as the first argument we call it 'self'
# 2. Classmethod automatically parse the class as the first argument we call it 'cls'
# 3. Static method don't pass anything automatically 
class Employee:
	num_of_emps = 0 
	raised_amount = 1.04 
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'

		Employee.num_of_emps += 1 

	def fullname(self):
		return '{} {}'.format(self.first, self.last) 

	def apply_raise(self):
		self.pay = int(self.pay * self.raised_amount)

	@classmethod
	def set_raise_amt(cls, amount): # as 'self' pyhton has class instence alled 'cls' we cannot use class 
									# because it has a different meaning as we have used on teh very top
									# and 'class' is a keyword in python
		cls.raised_amount = amount

	@classmethod # SP1
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod # ST1
	def is_workday(day): # Remember scince static method wont take instance or the class you can the argument that you want to work with in this case it's 'day'
# to print out the nuber of the date of the week (weekday =0-6 / isoweekday = 1-7)
# print(tday.weekday()) # we get vale '0' because in python Monday is '0' and Sunday is '6'
# print(tday.isoweekday())# in 'isoweekday' monday is '1' and Sunday is '7'
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

emp_1 = Employee('Nishan', 'john', 50000)
emp_2 = Employee('Edmon', 'Dontest', 60000)
emp_3 = Employee('Count', 'Mondego', 80000)
# lets change the raise amount to 1.06
Employee.set_raise_amt(1.06) # no need to mention 'cls' in the brackets it's already excepts it, as smae'self' instance
# emp_1.set_raise_amt(1.06) # L1

print(Employee.raised_amount)
print(emp_1.raised_amount)
print(emp_2.raised_amount)
print(emp_3.raised_amount)
# As you can see now all the raises are equel to 1.06, because we ran the 'set_raise_amt' method we created 
# which is a classmethod, means we are now working with class instead of instence ('self') by setting up
# 'cls.raised_amount = amount' method
# You also can run the class method from instance too which gives you the same result line L1
# emp_1.set_raise_amt(1.06) instead of Employee.set_raise_amt(1.06)

# What if you get Employee information in the form of strings that is seperated by 'Hyphen' or 'Slash' or anything
# Then you need to parse the string before create new Employee
# Lets see an Example

emp_str_1 = 'Amara-John-65000'
emp_str_2 = 'Roy-Shadwell-45500'
emp_str_3 = 'Nimal-Lansa-20000'
# first you have to 'split' the strings in the employee attributes
# first, last, pay = emp_str_1.split('-')
# then make new variable call new_emp_1 or what ever you would like
new_emp_1 = Employee.from_string(emp_str_1) # SP2
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)
# lets print this up
# print(new_emp_1.email)
# print(new_emp_1.pay)# as you can see it printed out as perfect as we expected
 # But it's an hectic approch to do this everytime Employees using this kind of string informations and parse 
 # through for individual employees
 # In order to make it right we have to use method call 'Alternative Constructor' means that allows them to parse
 # in the string and we can create the employee for them
 # First we should create a new classmethod (Related Sectors SP1-SP2)    
    
print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_2.email)
print(new_emp_2.pay)
print(new_emp_3.email)
print(new_emp_3.pay)
print("")
print("....................................Statis Method............................................")
#lets see the searching date is a week day or not (Related Sectors ST1-ST2) 
import datetime # ST2
my_date = datetime.date(2015, 4, 23)
print(Employee.is_workday(my_date)) # It gives 'True' value means, it's weekday
# remember if you are not using 'instence' or 'class' anywhere within the function it's advisable to use
# 'static method'.






