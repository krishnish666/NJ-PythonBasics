''' Class Veriables are variables which share among all the instences on a class, where instance variables
are unique to each other instances like name pay email etc.. where class variables are the same for 
each instences.
''' 

class Employee:
	num_of_emps = 0 # c1
	raised_amount = 1.04 # b1
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'

		Employee.num_of_emps += 1 # c2

	def fullname(self):
		return '{} {}'.format(self.first, self.last) # b2
# lets add a payraise method and our method automatically take in the instances by using call 'self'
	def apply_raise(self):
		self.pay = int(self.pay * self.raised_amount)
# and lets print this out as of below

emp_1 = Employee('Nishan', 'john', 50000)
emp_2 = Employee('Edmon', 'Dontest', 60000)
emp_3 = Employee('Count', 'Mondego', 80000)
# print(emp_1.pay) # basic pay
# emp_1.apply_raise() # applied thr rais
# print(emp_1.pay) # as you can see the raised amount '1.04' is added to 'emp_1' basic pay which is 52000
# now what if we want to print out the rasied amouunt, which is hidden benith the above method
# in order to do that just copy that raise amount '1.04' and past under the 'class Employee' with a class 
# variable 'raised_amount = 1.04', but if you apply 'raised_amount' within the 'self.pay = int(self.pay * raised_amount)'
# it wont work, instead you have to run it through either from class or 'self' instance as pentioned below
# 1. self.pay = int(self.pay * Employee.raised_amount)
# 2. self.pay = int(self.pay * self.raised_amount) lets change above method as shown here line b1 & b2

print(Employee.raised_amount)
print(emp_1.raised_amount)
print(emp_2.raised_amount)
print(emp_3.raised_amount)
# as you can see that i can access my class variable through both my class and instences as well, 
# What is going on here is that when we going to access an attribute on an instence, it will first check 
# that the instences contains are attributes or if it doesn't then it will see the class or any class that 
# Inheritance from, contains that attribute.
# lets make it more clear
# print(emp_1.__dict__) # as you can see,it prints out all the attributes (names,pay,e-mail except 'raised_amount')
# print(Employee.__dict__) # as you can see,it prints out'raised_amount' attribute as well with other extra stuff)

# lets change the raised_amount and print out the attributes

# Employee.raised_amount = 1.05
# emp_1.raised_amount = 1.05
# print(emp_1.__dict__)# to get the raised amount attribute for emp_1 

# print(Employee.raised_amount)
# print(emp_1.raised_amount)
# print(emp_2.raised_amount)
# Now you can see that it change the raised amount for the class and all of the instences
# But if you change the raised amount for 'epm_1 instence', it changes only the emp_1 attribute
# if you print name space 'print(emp_1.__dict__)' under the 'emp_1.raised_amount = 1.05' it will show
# 'raised_amount' attribute.
# Since we didn't set the raised_amount attribute for Employee, it won't show the 'raised_amount' attribute
# instead we set it to 'instence emp_1'
# By keeping 'self' intence, it gives the ability to change the individual instences if you want to
# Lets see how to count number of employees as we add new employees along, represent the lines c1 & c2 & c3
print("")
print("Number of Employees are",(Employee.num_of_emps)) # c3 (This will show there are three employees already in the list)

