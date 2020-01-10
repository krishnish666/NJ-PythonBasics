print("...............................Class Inheritance Method....................................") 
''' Inheritance allows us to inherit attributes and Methods from parent class, so it's important that we 
can create sub classes and access all the attributes and methods in sub classes without effecting the 
parent class''' 

# Lets create Developers and Managers under under Employee class line D1 & M1

class Employee:
	raised_amount = 1.04 
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last) 

	def apply_raise(self):		
		self.pay = int(self.pay * self.raised_amount)

class Developer(Employee): #D1 - Developer sub class inherits attributes from Employee class by using (Employee)  
	raised_amount = 1.20 # DM1
# Lets see without passsing any methods under Developer class, and print Employers e-mail ids whether to see
# Developer sub class is inheritted from parent class which is "Employee"	
	def __init__(self, first, last, pay, prog_lang):# DL1
		super().__init__(first, last, pay) 
		# Employee.__init__(self, first, last, pay)
		# You can use both method to call above common attributes rather than type all over again as in Employee class
		self.prog_lang = prog_lang 

class Manager(Employee):# M1
# lets give Manager Class some priviladges to access and'add/remove' employers under 'Msnsger Sub Class' 
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = [] # you cannot use immutable lists like 'Dict. or Tuples' as default arguments
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self): #P1
		for emp in self.employees:
			print('--->', emp.fullname())

# dev_1 = Developer('Nishan', 'john', 50000)
# dev_2 = Developer('Edmon', 'Dontest', 60000)
# dev_3 = Developer('Count', 'Mondego', 80000)
# lets create developers by changing the above Employee to Developer
 
# print(dev_1.email)
# print(dev_2.email)
# print(dev_3.email) 	# as you can see it prints out the email ids of the employers from the parent class
					# means 'developer class' inherits from the 'Employee class'
# lets print out 'Method Resolution Order' od Developer class by using 'help' function
# print(help(Developer))
# as you can see you will get lot of attributes and methods for Developer sub class through inheritance method
# Lets see to print out the raise amount for sub class developers before assigne any arguments within the 
# 'sub class of Developer'

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# As you can see, since we haven't assign any modification for the raise_amount within Developer class, it goes
# and inherit the already assigned raise_amount attribute from the parent class which is (Employee class)

# Lets change our developers rais-amount by 1.20 in the sub class Developer and print out the values Line DM1
# Now you can get the results with the modified raised_amount in Developers pay scheem

# now lets see whether it effected any way to the parent class by changing as below;
# dev_1 = Employee('Nishan', 'john', 50000)
# dev_2 = Developer('Edmon', 'Dontest', 60000)
# dev_3 = Developer('Count', 'Mondego', 80000)
 
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)# raised the amount as per Employee class assignment
# print("")					
# print(dev_2.pay)
# dev_2.apply_raise()# raised the amount as per Developer Sub Class assignment
# print(dev_2.pay)				
# print("")
# print(dev_3.pay)
# dev_3.apply_raise()# raised the amount as per Developer Sub Class assignment
# print(dev_3.pay)

# lets see how we give priviladge for developer class to add some more attributes that 'Parent or Employee' 
# class doesn't have as an ex: "Programming Language" attribute by using (__init__) method as above 
# (Refer Sector: DL1)
# Lets add some programming languages to intialize for passed in, and print out first Emp email & Language
dev_1 = Developer('Nishan', 'john', 50000, 'Python')
dev_2 = Developer('Edmon', 'Dontest', 60000, 'Java')
dev_3 = Developer('Count', 'Mondego', 80000, 'Visual Basics')

# lets create a new manager and lets include the employee dev_1 from 'developer class' under managers supervision
mgr_1 = Manager('Roy', 'John', 90000, [dev_1]) 

# print(dev_1.email)
# print(dev_1.prog_lang)
# logic behind the scene, once you run this, it will go all the way up to the 'Parent Class init' method
# and set all of those attributes within there and it also set our programming language within our 
# 'Developer init' method there.
print(mgr_1.email)

# lets add some more employee to the Manager supervision
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)

# lets print out all teh employees this manager supervisors
# mgr_1.print_emps() # refer P1 call 'print_emps() function'
# as you can see it displayed 'dev_1 & dev_2 & dev_3' employees full names under mgr_1

# lets remove an employee from the Manager supervision
mgr_1.remove_emp(dev_1) # employee "dev_1 Nishan John" is removed from the list
mgr_1.print_emps()
print("...........................................................................................")
  # Python has two built in functions called 'isinstance & issubclass'

# "isinstance method"
print(isinstance(mgr_1, Manager)) # mgr_1 is an instance of the Manager class, here it gives "True" value
print(isinstance(mgr_1, Employee)) # mgr_1 is an instance of the Employee class, here it gives "True" value
print(isinstance(mgr_1, Developer)) # mgr_1 is an instance of the Employee class, here it gives "False" value
# it gives 'False' because as we know both Developer & Manager inherites from Employee class, they aren't part
# of eachother inheritance.
print("...........................................................................................")
# "issubclass method"
print(issubclass(Developer, Employee)) # Developer is a Subclass of the Employee class which is "True"
print(issubclass(Manager, Employee)) # Manager is a Subclass of the Employee class which is "True"
print(issubclass(Developer, Manager)) # Developer is a Subclass of the Manager class which is "False"



									







