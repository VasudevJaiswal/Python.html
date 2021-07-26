# Chapter 4 – Lists and Tuples ?
# Python Lists are containers to store a set of values of any data type.

#List Slicing ?
# friends = [‘Apple’, 'Jaiswal', ‘Vasudev’, 7, False, 45, 3.5] 

a = [1,2,3,4,55,6]

#Print the list using the print() Function 

print(a)

# Access using index using  a[0], a[1]

print(a[0])  # Index in list start with 0 as String return is - 100
print(a[1])  # return is - 1

#Change the value of list using the a[0] functionn

a[0] = 100   # WE use to print seperate list of index in python

# We can create a list with items of different types

c = [45,"Vasudev", False, 6.9]   # it is valid a list with different item
print(c)

# list Slicing 
friends =  ["Vasudev", 18,"bsc",63.66,True]
print(friends)
print(friends[0:4])   # the return is -- ['Vasudev', 18, 'bsc', 63.66]
print(friends[:-4])   # The return is --- ['Vasude']



# List Method 


# List Indexing 
# A list can be index just like a string.
l1 = [1,8,7,2,21,15]

# 1. sort() – updates the list to [1,2,7,8,15,21]

l1 = [1,8,7,2,21,15]
print(l1)
l1.sort()    # sort to highest
print(l1)   #The result is  return -- [1, 2, 7, 8, 15, 21]


# 2. reverse() – updates the list to [15,21,2,7,8,1]

l1 = [1,8,7,2,21,15]
l1.reverse()    # reverse the lists 
print(l1)  # return -- [15, 21, 2, 7, 8, 1]

# 3. append(8) – adds 8 at the end of the list

l1 = [1,8,7,2,21,15]
l1.append(45)     # Adds at the end of the lis
print(l1)       # retrun -  [1, 8, 7, 2, 21, 15, 45]

# 4. insert(3,8) – This will add 8 at 3 index

l1 = [1,8,7,2,21,15]
l1.insert(1,544)   # 544 update in this line at index 1st character 
print(l1)          # retrun is -- [1, 544, 8, 7, 2, 21, 15]

# 5. pop(2) – It will delete the element at index 2 and return its value

l1 = [1,8,7,2,21,15]
l1.pop(2)   # index 2 is removed 
print(l1)   # return is --  [1, 8, 2, 21, 15]

# 6. remove(21) – It will remove 21 from the last

l1 = [1,8,7,2,21,15]
l1.remove(21)  # Removes elements from the list
print(l1) # return - -[1, 8, 7, 2, 15]





