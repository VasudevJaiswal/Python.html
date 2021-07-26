# Tuples in Python ? 
# A tuple is an immutable (can’t change or modified) data type in Python. 

# Creating the tuples using ()
t = (1,2,4,5)

# t1 = () # Empty tuple
t1 = ()

# t1 = (1)  #Wrong way to declare a tuple with single element 

t1 =(1,)  # Tuple with single Elements

print(t1) 
#Printing the elements of a tuple
print(t)

# Cannot update the values of a tuple
# t[0] = 20  return is --- error 


# Tuples Method 

t2 = (1,2,4,5,4,1,2,1,1,1)

# count(1) – It will return the number of times 1 occurs in a.f
print(t2.count(1))

# index(1) – It will return the index of the first occurrence of 1 in a.
print(t2.index(5))   # return == 3 is for seeing the indexing