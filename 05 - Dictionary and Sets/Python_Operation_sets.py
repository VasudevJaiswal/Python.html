# Operations on Sets ?  
# Consider the following set: 

S = {1,8,2,3}

# Len(s) : Returns 4, the length of the set

S = {1,8,2,3}
print(len(S))  #Length of the Set


# remove(8) : Updates the set S and removes 8 from S

S = {1,8,2,3}
S.remove(8) #Remove of the Set
print(S) 


# pop() : Removes an arbitrary element from the set and returns the element removed.

S = {1,8,2,3}
print(S.pop())  # Returs the Removed Elements of the set 


# clear() : Empties the set S

S = {1,8,2,3}
print(S.clear()) #the return is clear or None


# union({8, 11}) : Returns a new set with all items from both sets. #{1,8,2,3,11}

S = {1,8,2,3}
print(S.union()) 


# intersection({8, 11}) : Returns a set which contains only items in both sets. #{8}

S = {1,8,2,3}
print(S.intersection())