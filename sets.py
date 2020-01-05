print (" sets are dictionaries & using Curly Brackets {}")
#set_1 = {'History','Science','Maths','Relegion','English','Social Studies'}
#print(set_1) # Notice that everytime you run this list, the order of the value changes

# if i create another list and add a duplicate value, it throws that duplicate value away.
set_2 = {'History','Science','Maths','Relegion','English','Social Studies'}
set_3 = {'Logic','Science','PT','Music','English','Art'}
print(set_2) # This will erase duplicate values and display the rest
# if you want to see common subjest (values) in both lists by using '.intersection' method
print(set_2.intersection(set_3))
# if you want to see the unique subjest (values) to each lists by using '.differance' method
print(set_2.difference(set_3)) # Unique subjects in Set_2 List
print(set_3.difference(set_2)) # Unique subjects in Set_3 List
print(set_3.union(set_2)) # To combine both lists togeather by using '.union' method
# create an empty Set
#empty_set = {} # This is not an empty set but this is an empty dictionary
#empty_set = () # This will create epmty set
print (".....................................................................")
# Add values for an empty list Ex 001
#y =[]
#for x in range(0,25,2):
#	y.append(x)
#	print(y)

#print (".....................................................................")
# Add values for an empty list Ex 002
#Sub001 = []
#for x in set_2:
#	Sub001.append(x)
#	print(Sub001)
# Add more values using 'update' method
set_2.update(['Electronic','Bio','Sulogy','Science'], set_3)
print(set_2)

# Ommit values using 'Remove and Discard' method
Num1 = {1,2,6,8,7,9}
Num2 = {1,3,6,10,7,5}
Num3 = {8,2,11,5,7,9}

#Num1.remove(8) # Here you need to mentioned the value you want to remove not the index number
#print(Num1, '\n')
#Num1.discard(10) # The differance is the 'discard' method is, it wont throw any error 
				# message when discard wrong value which is not in the list 
#print(Num1)

# if you want to see common (values) in all lists by using '.intersection' method compared to 'Num1 List'
Num4 = Num1.intersection(Num2,Num3)
print(Num4)

# want to see the unique (values) only in 'Num1 list' compared to 'Num2 List' '.differance' method 
Num4 = Num1.difference(Num2)
print(Num4) # It shows an empty list because there is no different values which not in the other two lists

# This method shows all the different or ununique numbers of both 'Num1 & Num2' lists where as above method
# shows only Num1 list' ununique values compared to 'Num2 List
Num4 = Num1.symmetric_difference(Num2)
print(Num4, '\n')

# Now we create a new list with duplicate valies
l1 = [1,8,7,11,8,2,3,5,7,2]
# Now we will make a Set throwing all the duplicates
l2 = set(l1)
print(l2)
# Now again change this set list to normal list as original abov
l2 = list(set(l1))
print(l2, '\n')

# Lets make a Example with names
Employees = ['Nishan', 'John','Charith','Niluk', 'Roy','Niroshan','Vishmi', 'Asela','Erick']
Gym_Members = ['Piyal', 'John','Amara','Adeepa', 'Roy']
Developers = ['Charith', 'Niroshan','Gaya','Koorey', 'John', 'Asela', 'Piyal']

# Lets see the members who are in both Gym and Developer catogary
result = set(Gym_Members).intersection(Developers)
print(result) # Result is 'Piyal & John'

# Lets see the members who are not nither in Gym nor Developers catogaries
result1 = set(Employees).difference(Gym_Members,Developers)
print(result1) # Results are 'Niluk, Nishan, Erick, Vishmi'

# this method create set and find results are much eazier than using if or for functions or statements



