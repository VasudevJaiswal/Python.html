# Chapter 06 – Conditional Expressions ?

# Sometimes we want to play pubg on our phone if the day is Sunday.

# Sometimes we order Ice-cream online if the day is sunny.

# Sometimes we go hiking if our parents allow.

# All these are decisions that depend on the condition being met.

# In python programming too, we must be able to execute instructions on a condition(s) being met. This is what conditions are for!

# If else and elif in Python
# @ @ @ @IMP If else and elif statements are a multiway decision taken by our program due to certain conditions in our code.

# Syntax: ?


# if (condition1):		 // if condition 1 is true
# 	print(“yes”)
# elif (condition2):		// if condition 2 is true
# 	print(“No”)
# else:				// otherwise
# 	print(“May be”)

var = int(input("Enter the Integers"))
if(var>46):
    print("The value of var is greater than 3")
elif(var>7):
    print("The value of var is greater than 7")
else:
    print("The value of a is nor 3 or nor 7")


    # "Age valid for drink if elif or else "

    age = int(input("Enter Your Age:"))
if(var>=18):
    print("You are Eligible for drink")
elif(var=18):
    print("You are Eligible for drink")
else:
    print("You are not Eligible for drink")

# Multiple If Statements  - Nested If statements 

let a = int(intput("Enter yuor Integers"))
if a>5:
    print("true")
if a>7:
    print("false")
if a>10:
    print("true")
else:
    print("false")


# Important Notes:

# There can be any number of elif statements.
# Last else is executed only if all the conditions inside elifs fail.