# String Slicing: ?
# A string in Python can be sliced for getting a part of the string.

first_Name = "Vasudev"
last_Name = "Jaiswal"
# Concatenating two String 
Full_Name = first_Name +  last_Name
print(Full_Name)

# Slicing in Python
name ="Vasudev"
print(name[4])  #Starting string and int 0 [0-4 = V,a,s,u,d]
# The index in a string starts from 0 to (length-1) in Python. To slice a string, we use the following syntax:
# Slicing ?
print(name[0:4])  # In this method : colon use for[0 to 4 - [0:4] ] then Result is Vasu

# Negative Indices: ?
# Negative indices can also be used as shown in the figure above. -1 corresponds to the (length-1) index, -2 to (length-2).

name1= "Vasudev"
print(name1[-7:-3])  #The result is  Vasu 

# Slicing with skip value?
# We can provide a skip value as a part of our slice like this:

d = name[1:8:1] # Skippped the one letter because skiddped value :1 in the last digit 
print(d)

# Other advanced slicing techniques 

word = ‘amazing’

word[:7] or word[0:7]      #It will return ‘amazing’

word[0:] or word[0:7]      #It will return ‘amazing’