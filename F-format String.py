customer = {'name': 'Jonnyb', 'age': '35', 'ID No': 'HMH129'}

# Basic method of formatting strings by using 'Concatenating' method
sentence = 'My name is ' + customer['name'] + ' and i am ' + customer['age'] + ' years old' + ' and my ID Number is ' + customer['ID No']
print(sentence)

# Now we use bit advanced and convenient way of formating strings by using 'format' method
# Method 001
sentence = 'My name is {} and i am {} years old and my ID Number is {}.'.format(customer['name'], customer['age'],customer['ID No'])
print(sentence)

# Method 002
sentence = 'My name is {0} and i am {1} years old and my ID Number is {2}.'.format(customer['name'], customer['age'],customer['ID No'])
# in the above method {0},{1},{2} represents the first,second and third values in the list to be placehold in the relevent brckets in the sentence
print(sentence)
 # Lest see another different example of place order the values
# tag = 'hi'
# text = 'This is a Headline'

# sentence_1 = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence_1) # This will print out a HTML coding tags

# Method 003
sentence = 'My name is {0[name]} and i am {1[age]} years old and my ID Number is {2[ID No]}.'.format(customer, customer, customer)
print(sentence)

# Method 004
sentence = 'My name is {0[name]} and i am {0[age]} years old and my ID Number is {0[ID No]}.'.format(customer)
print(sentence)
# This will pass the customer dictionary to all our place orders and access the name.age, and so on by replace all to {0}s
 
# Method 005
# Will make a list and directly access the place orders by index numbers of the list
Li = 'John', 38, 'HMH129'
sentence = 'My name is {0[0]} and i am {0[1]} years old and my ID Number is {0[2]}.'.format(Li)
print(sentence)

# Method 005 (same cann be used for attributes also)
class Agent():
	def __init__(self, name, age, ID_No):
		self.name = name 	# name attribute
		self.age = age 		# age attribute
		self.ID_No = ID_No 	# ID_No attribute

A1 = Agent('Nishan', '38', 'HMH129')
sentence = 'My name is {0.name} and i am {0.age} years old and my ID Number is {0.ID_No}'.format(A1)
print(sentence)
print("")
print("......................Use key word attribute for formatting..................................")
# Method 006 use 'key word argument' for formatting
sentence = 'My name is {name} and i am {age} years old and my ID Number is {ID_No}.'.format(name='Charith', age='38',ID_No='NYK123')
print(sentence)
print("")
print("...............Use Unpacking(**) Dictionary list method for formatting.........................")

Guests = {'name': 'Jonnyb', 'age': '38', 'ID_No': 'LMM589'}
sentence = 'My name is {name} and i am {age} years old and my ID Number is {ID_No}.'.format(**Guests)
# '**' represents unpack the dictionary list
print(sentence)
print("")
print(".................................Format Number through loops...................................")

for n in range(1, 11):
	# sentence = 'The value is {}'.format(n)
	# if you want two or more digit list
	sentence = 'The value is {:02}'.format(n)
	print(sentence)
print("")
# Format decimal numbers
n1 = 3.524666
sentence = 'n1 is equel to {:.2f}'.format(n1) # in order to place two desimal places use ':2f' command
print(sentence) 
print("")
# print large numbers with ',' seperated
sentence = '1 MB is equel to {:,} bytes'.format(1000**2) # to get ',' seperated;
sentence2 = '1 MB is equel to {:,.2f} bytes'.format(1000**2) # to get ',' seperated and two desimal vale;
print(sentence)
print(sentence2)
print("")
print(".........................Formatting strings using 'f'(formated string)..........................")
# format method
first_name = 'Devapriya'
age = '38'
gender = 'Male'
# sentence = 'My name is {} and i am {} years old and my gender is {}.'.format(first_name, age, gender) 
# print(sentence)

# Lest see how to get value with more advanced way by using 'f' string method
# you can directly put place orders in the curly brackets using 'f' or 'formated' strins
sentence = f'My name is {first_name} and i am {age} years old and my gender is {gender}.'
# not only that by using 'f' string method you can pass function in it, lets make upper case of our 'first_name'
sentence1 = f'My name is {first_name.upper()} and i am {age} years old and my gender is {gender.upper()}.'
print(sentence)
print(sentence1)
print("")
# lets see using some dictionary values using 'f' string
# First we use 'format' method
client = {'name': 'Jonnyb', 'age': '35', 'ID No': 'HMH129'}
client_list = 'My name is {} and i am {} years old and my ID Number is {}.'.format(client['name'], client['age'], client['ID No'])
print(client_list)
# Lets see to get the values using 'f' string
# client_list = f'My name is {client['name']} and i am {client['age']} years old and my ID Number is {client['ID No']}.'
# when you run this, you will get an error message, since your single quotes'name' within the place orders will
# be terminated by the 'f' string single quotes, so you have mention your place orders with double quotes 
client_list = f'My name is {client["name"]} and i am {client["age"]} years old and my ID Number is {client["ID No"]}.'
# Now single quotes no longer conflict with place orders double quotes
# or you van do the other way arround by keeping the place orders in the single quotes and make double quotes in the 'f' string
client_list2 = f"My name is {client['name']} and i am {client['age']} years old and my ID Number is {client['ID No']}."
print(client_list)
print(client_list2)
print("")
print("............................Calculations using 'f'(formated string)..............................")
calculation = f'4 times 11 is equal to {4 * 11}'
print(calculation)
# calculation through for loop using 'f' string
for n in range(1, 11):
	cal = f'The value is {n:02}'
	print(cal)
# calculate floating points using 'f' string
pi = 8.336464
cal1 = f'Pi is equal to {pi:.2f}'# Pring floting number with two digits
print(cal1)













