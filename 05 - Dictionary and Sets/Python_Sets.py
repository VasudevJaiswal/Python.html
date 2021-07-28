# Sets in Python ? 
# Set is a collection of non-repetitive elements.

import collections


a = {1,3,4,5}
print(a)
print(type(a))  # This is type of set <class set >

# Sets cannot contain duplicate values 
b = {1,3,4,5,1,1,1}
print(a) #Return is 1,3,4,5 because of set doesn't collect repeat elements



# this syntax create Empty Dictionary not Empty set 
c = {}
print(c) 

#An empty  set can be created using the below syntax : EMPTY SET 
b1 = set()
print(type(b1))  #this is empty set <class set>
b1.add(4)
b1.add(5)
b1.add(5) #The set is collections of not reppative elements
print(b1)

# Properties of Sets ?
'''1. Sets are unordered # Elements order doesn’t matter
2. Sets are unindexed # Cannot access elements by index
3. There is no way to change items in sets
4. Sets cannot contain duplicate values '''


