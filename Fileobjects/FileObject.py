print("..............................Lets read (r) a file.........................................")
# f = open('sampletext.txt', 'r') # we going to open a file for reading 'r' in the same CWD
# print(f.name) # to print out the name of the file
# print(f.mode) # to print out the mode of the file ('r' / 'w' / 'a' etc...)
# # print(f.name) # to print out the name of the file
# f.close() # make sure you close the file once you open it

# we will use context manager to open a file, then you don't have to manually close the file at the end
# using 'with open' command
# with open('sampletext.txt', 'r') as f: # now you have to work within this context manager you cannot call
										# the 'print('f.read()) method or any other outside from the context manager
	# f_contents = f.read()
	# f_contents = f.readlines() # this will diplay the contents in a list
	# f_contents = f.readline() # this will diplay the contents line by line
# What if you want to print out spesific amount of data in your file content
	# f_contents = f.read(100)# this will show you the first 100 characters in your file contents
	# print(f_contents)
	# print("")# if copy and past down these command lines, it will print out the rest of the 100 characters

# what if we want to print out large list of contents through a loop that iterate to small bush of contents
# using pass a variable
	# size_to_read = 10
	# f_contents = f.read(size_to_read)
	# # print(f.tell())# to find out which position you are in, in this case you are in 10th position
	# while len(f_contents) > 0:
	# 	print(f_contents, end="/")# don't print like this because it will take a infinite loop which is never ends
	# 	f_contents = f.read(size_to_read)	# call the this command again in order to exit from infinite loop and 
											# search for the next set of contents within the while loop. 
		# print(f.tell())# this will show you all the positions that we have seperated by slash '/'
# inorder to clear what is happening will put an '/' inside the end and make the size to read to 10
# as you can see the file contents seperated by '/' for every 10 characters.

# what if we want to read a huge file with lot of contents, you can iterate and use for loop function
	# for line in f:
	# 	print(line, end='')
	# print(f) # what this does is, it runs line by line with regular intervals while maintaining your PC ram constrain.


with open('sampletext.txt', 'r') as f:
	# f_contents =f.read()

	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(f_contents, end='')
# 
	# # f.seek(0)# you can see the second read is started back from the begining, you can change the count and see;
	f.seek(25)# you can see the second read is started back from the begining, you can change the count and see;

	f_contents = f.read(size_to_read)
	print(f_contents) # you can see it printed out chracters upto 20 and as you can see second read is started from the first read is ended
	# what is you want the second reading from the very begining by using "seek" command
print("")
print("..............................Lets write (w) a file.........................................")

''' Remember if you write to a file which is existing will overwrite you file and erase all the previos
data and input whatever you write in it. Secondly: If going to write a file which is not existing will be 
created anew file as per your assigne "filename" in the CWD. Thirdly: while command is set to 'r', you cannot 
write a file unless you change it to write 'w' mode.'''

# with open('sampletext002.txt', 'w') as f:
# 	f.write('Test') # as you can see this command created new .txt file as we mentioned and write 'Test' in it
# 	f.seek(0) # as you can see if you use seek method it will overtite the previous text, seek function not working considerable fine with file write method 
# 	# f.write('Test') # you can write anything in it like this 
# 	f.write('R') # This will seek and replace only the first character in the previous 'test' content

# lets will pull 'w' & 'r' method together and write all the contents from original filr to new file.
# using nested 'while open' function 
# with open('sampletext.txt', 'r') as rf:
# 	with open('sampletext002.txt', 'w') as wf:
# 		for line in rf:
# 			wf.write(line) 
# as you can see all the contents which were in the original file copied to the new file

# lets do this for a picture object which has slight different method for it
# you have to use the method 'byte' mode means you have to open through bineay mode as 'rb' & 'wb' otherwise you get an error
# 'utf-8 codec can't decode byte 0xff in position 0: invalid start byte 
# with open('27.jpg', 'rb') as rf:
# 	with open('lantonlady.jpg', 'wb') as wf:
# 		for line in rf:
# 			wf.write(line) 

# instead of read line by line will read chunk or bunch of lines by lines, this can do to pictures too
# as we did for f_contents read file as 'size_to_read = 100' use the same procedure:
with open('27.jpg', 'rb') as rf:
	with open('lantonlady.jpg', 'wb') as wf:
		chunk_size = 4096 # you give any valuve you want
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)# in order to escape from infinite loop and go for the rest of the lines through while loop
			

			
