Subjects = ['History','Science','Maths','Relegion','English','Social Studies']

for item in Subjects:
	print(item)

print (".....................................................................")

# if we want to return value with the index number
#for index, Subjects in enumerate(Subjects):
	#print(index, Subjects)

# if we want to return value with the index number starting from one usine 'start=1' method
#for index, Subjects in enumerate(Subjects, start=1):
	#print(index, Subjects)

# if we want the items seperate from ',' in the same line using '.join' method
#Subjects_str = ', '.join(Subjects)
#print(Subjects_str)

#Subjects_str = ' - '.join(Subjects)# if you want to seperate by hyphanate '-' mark
#print(Subjects_str)

Subjects_str = ' / '.join(Subjects)# if you want to seperate by Slash '/' mark
print(Subjects_str)

#if you want to bring back to to original list removing all these seperators by using '.split' method

new_list = Subjects_str.split(' / ')
print(new_list)

print (".....................................................................")


