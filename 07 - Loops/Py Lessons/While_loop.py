# While loop

# The syntax of a while loop looks like this:

''' while condition:
    #Body of the loop '''

# The block keeps executing until the condition is true/false
# In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed, otherwise not!

# If the loop is entered, the process of condition check and execution is continued until the condition becomes false.

i = 0
while i<10:
    print("Yes" + str(i))
    i = i+1

print("Done")

# Break Statements in Python 

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Continue Statements in Python 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# Else Statements IN Python 

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

  # Note that number 3 is missing in the result