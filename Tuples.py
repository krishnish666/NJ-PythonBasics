print (" Lists are Immutable & using Parenthesis ()") 
Subjects_1 = ('History','Science','Maths','Relegion','English','Social Studies')
Subjects_2 = Subjects_1

print(Subjects_1)
print(Subjects_2) # Both values look the same in both Tuple lists

# Let's see whther we cound change the value with another value as we did in the list
Subjects_1[0] = 'Chemestry'
print(Subjects_1) 	# we will get an ypeError: 'tuple' object does not support item assignment,

''' 
 Note: Tuples are immutable and we cannot change,append,remove,basically you cannot mutate the values
 in the Tuples but your can do loop through it using 'for' / 'while' loopa.
'''

# creat empty Tuples
empty_tuple = ()
empty_tuple = tuple() # This two methods will create epmty Tuples








