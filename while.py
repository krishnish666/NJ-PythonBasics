condition = 1

# whatever the condition is, if it is less than 10 print them all
# #(colon ":" indicates after while loop because whatever print after it is a part of while function)
while condition < 10: 
	print (condition)
	# count one by one to the bottom Ex: (1),1+1=(2),2+1=(3) etc....
	condition += 1 # is equel to "condition = condition + 1"
# if you want to print "Hellow world" for 10 times;
N = 1 # initialization of the variable

while N <= 10:
	print ("Hellow world ",end="") # if you want to print the value with count, you have enter 'N' as shown
	# creating nested while loop, loop inside a loop
	# remember that when you run this, first it prints inner loop function and outher loop next.
	# (end="") will print teh values in the same line Horizontally
	J = 1 # (by placing the intialization here will print "Sucks" with everly linve of above)
	while J <= 6:
		print("Sucks ",end="") # if you want to print the value with count, you have enter 'J' as shown
		J += 1
	N += 1
	print() #(we have to print at the end after all the above funcions(arguments) for new line)
	# Above function will print as "Hellow worldSucksSucksSucksSucksSucksSucks" for 10 times
	# Process flow is as below
	# 1, it will prints "N" value "Hellow World" first since (N = 1) amd jump to "J"
	# 2. it will prints "J" value "Sucks" second in front of "N" value 
	# 3. Since "J" is <= 6, it loops and print 6times and jump back to "N" and start (N=2)
	# 4. again run the same process as above (as i have mentioned b4 it runs the inner loop and jump to outer loop) 






# while True: is infinit looping within the function assigned till it meet it's target or requirement or unless you break in some point 
# Example
#print ("Starting...................!") # 1 Step
#while True:
#	print ("* top of loop*") # 2 Step
#	x = input("Enter 'q' to quit: ")
#	if x == 'q': # 3 Step
#		print("Quitting........!") # 4 Step
#		break
#	print("Continuing.....!") # 6 Step (if it is not equel to 'q' then it will continue and 
#							  # start the process all over again)
#	
#print ("Ending.....!") # 5 Step

# Another Example in Def function
def get_answer(prompt):
	while True:
		answer = input(prompt).strip()
		if answer in ('Yes','No'):
			return answer
print(get_answer("Yes or No? "))



