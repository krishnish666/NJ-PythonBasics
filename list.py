# Make a list of Subjects and print the values " Lists are mutable"
print (" Lists are Mutable & using Square Brackets []")
Subjects = ['History','Science','Maths','Relegion','English','Social Studies']
Num = [0,2,4,6,10,7,9,45,71,91] 
#print(Subjects)
#print (".....................................................................")
# Print the length (number of Values) in the list using 'len' function
Subjects = ['History','Science','Maths','Relegion','English','Social Studies']
# To change  value of the list with another value
Subjects[0] = 'Chemestry'
print(Subjects)
#print(len(Subjects))
# To print the first value in the list using index number
#print(Subjects[0])
# To print the forth value in the list using index number
#print(Subjects[4])
# To print the last value in the list whixh is 'Social Studies' in this case using index number (-1)
#print(Subjects[-1])
# To print range of values 'from begining to third excluding the third value' in the list using index number
#print(Subjects[0:3])# Third value is not showing but '0-to-2' it stops printing third value
#print(Subjects[2:])# this will print from second to all the way to the end value by keeping empty in the brackets
#print(Subjects[:3])#same for the other way too
print(Num[0:10:2]) # if you want to print the list by skipping one element in the liist represent by '2'
print(Num[0:10:3]) # if you want to print the list by skipping one element in the liist represent by '3'

#print (".....................................................................")
# if you want to add an item to the end of the list by using 'append' command
#Subjects.append('Art')
#print(Subjects)
# if you want to add an item to a spesific location in the list using 'insert' method
#Subjects.insert(2, 'Electronics')
#print(Subjects)
#print (".....................................................................")
#Subjects2 = ['Music', 'PT']
# What if we want to append or insert the second list within the first list to the begining
#Subjects.append(Subjects2)
#print(Subjects) # this will add the entire list within the first list items at the end of the first list

#Subjects.insert(0, Subjects2)
#print(Subjects) # this will insert the entire list within the first list items

# what if we want add on the items within the first list by using 'extend' method
#Subjects.extend(Subjects2)
#print(Subjects)# this will add only the items of the second list

#print (".....................................................................")
# Remove item or items from the list
#Subjects.remove('Social Studies')
#print(Subjects)

# there is another way to remove last item in the list which is 'PT' in this case by using 'po' method
#Subjects.pop()
#print(Subjects)

#if you want to disply the value you have deleted by using pop, you have to make a variable as below;
#popped = Subjects.pop()
#print(popped)
#print(Subjects)

#print (".....................................................................")
# if you want to sort or reverse the list values
#Subjects.reverse()
#print(Subjects)# you can see the list from end to first and first to last

#Subjects.sort()
#print(Subjects)# you can see the list is been sorted out alphabatical order

# lets create number list and user sort and reverse methods in one line 
Numbers = [5,6,8,10,99,4,78,2,3,46,1]
Numbers.sort(reverse=True)
#Subjects.sort(reverse=True)
print(Numbers)
#print(Subjects)

Sorted_Subjects = sorted(Subjects)# This 'sorted' method will bring back our original list unsorted
print(Sorted_Subjects)
# find the minimum and maimum number & sum in the list]
print(min(Numbers))
print(max(Numbers))
print(sum(Numbers))
# fin the index number of the variable in the list
print(Subjects.index('Relegion'))
# to check whether the subject is in the list (Fales or True) using 'in' method
print('PT' in Subjects) # subject 'PT' is not in the list so it gives False feedback
print('English' in Subjects) # subject 'English' is in the list so it gives True feedback

# create Empty lists;
empty_list = []
empty_list = list() # This two methods will create epmty List

print (".....................................................................")

# Check the comparison of IDs each list using 'id' method
# First creat a nested list
test_list = [
				['First Name' , 1,2,3],
				['Second Name' , 4,5,6],	
				['Third Name' , 7,8,9]	
] 
print(test_list,)
# Now we will make a copy of the same list
test_copy = test_list
print(test_copy)
# Now create a function to get Id's of the lists
print('\n')
def disp_id():
	print ("Test_list ID: ", id(test_list))
	print ("Test_Copy ID: ", id(test_copy))
	# Lest add more lines and call for the ID's of first objects of both lists
	print ("Test_list[0] ID: ", id(test_list[0]))
	print ("Test_Copy[0] ID: ", id(test_copy[0]))
disp_id()
# As you can see both ID's are the same for different variables (test_list & test_copy) with the same data
# now if you change any data in one list will effect the other list and change the same
print('\n')
# To nake test_copy to different list with different ID, with using 'list' comand
test_copy = list(test_list)
# and now you call the disp_id function back, you can see different IDs
disp_id()
print('\n')
# But even you have different id in your cloned list, if you change a data in the original lis
# it will be changed the same in the cloned list, sice pyhton identify the both list's data in the same location 
# now we change a data and see
test_list[0][0] = 'Surname' # changed 'First Name' to 'Surname' in the test_list
print(test_list)
print(test_copy)
# As you can see changes has been done in the both lists
# lets see the ID's of the first object we change in the nested list by calling the disp_id function
disp_id() # you can see both objects ID's are the same even main list's ID's are different
# Now let's try to change the ID's of the objects by make an iteration to the list
# One way of doing it using 'for' method
print('\n')
test_copy = []
for item in test_list:
	test_copy.append(list(item))
	
disp_id()

