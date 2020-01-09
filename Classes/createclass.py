''' Inheritance: Inheritance allows you to define data and procedure in one place (in one class),
 and then override or extend that functionality later. For instance, in Python, I often see people 
 creating subclasses of the dict class in order to add additional functionality. 'Data' and 'Functions' associated
 with specific classes, we call then 'attributes' & 'Methods' '''

 # lets create an application for a compny representing the employees where individual attributes are assigned
 
class Employee: # Class are blue print of instances of that particular classes 
	# pass # This command in python indentify you just want to skip that for now without getting error during running the script 
	def __init__(self, first, last, pay): # email we coud concatenate with first and last names
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last) 	# pate the same command as below, but instead of 'emp_1'
														# we have to put instance 'self' so it work for all
		
# lets input the details of the employees down below respectively as of above
emp_1 = Employee('Nishan', 'john', 50000)
emp_2 = Employee('Edmon', 'Dontest', 60000)

# print(emp_1)
# print(emp_2)
# as you can see both output objects are unique to each other
# In this we are talking about instance variables which has unique values
# Now lets manually create instance variable for the employees
# emp_1.first = 'Nishan'
# emp_1.last = 'John'
# emp_1.email = 'Nishan.John@gmail.com'
# emp_1.pay = 50000

# emp_2.first = 'Edmon'
# emp_2.last = 'Dontest'
# emp_2.email = 'Edmon.Dontest@gmail.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)
# As you can see the e-mails are created for each employee instences, but using this this method you need to
# use lot of codes and class function is not gonna be more usefull if you do like this method
# inorder to make it more reliable and convenient, we use '__iniy__' method instead of 'pass' lets see how it works
print("")
print(emp_1.email)
print(emp_2.email)
print("")
# Lets print out the full name of an Employee using place orders
print('{} {}'.format(emp_1.first, emp_1.last))
# As you can see it printed out full name of the Employee1, but still it's too much to code
# inorder to make it more reliable we will make a method for 'fullname' with instance using'self'
# on top under the Employee class
print(emp_1.fullname())# now you can pring this way and make sure put (parenthesis) otherwise it print out
# the method instead of the attribute
print(emp_1.fullname) # without (parenthesis)
# this also printed out the fullname as above with less codings
# so if you want to print out emp_2, by simply change emp_1 to emp_2
print(emp_2.fullname())# when you use instance 'emp_1' with the method 'fullname', no need to mention 'self' 
# because it does it automatically
# remember if try to print fullnameas obove without mentioned'self' instance in 'def fullname()' method 
# you will get an eroor Typeerror: fullname() takes a 0 positional argumet but 1 was given  
# lets see what happens exactly when we print out emp_1 fullname
print("")
print(emp_1.fullname())
# in the background
print(Employee.fullname(emp_1)) # When you run, it will transform to the method 'Employee.fullname' and passes in
#'emp_1' as 'sels' and that's why we have 'self' for this method




