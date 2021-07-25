# Operators in Python 

# The following are some common operators in Python:

# Arithmetic Operators (+, -, *, /, etc.)
# Assignment Operators (=, +=, -=, etc.)
# Comparison Operators (==, >=, <=, >, <, !=, etc.)
# Logical Operators (and, or, not)

# Arithmetic Operators (+, -, *, /, etc.)

a = 3
b = 4
print("The Value of 3+4 Add  is ", a+b)
print("The Value of 3-4 Sub  is ", a-b)
print("The Value of 3*4 Mul  is ", a*b)
print("The Value of 3/4 Div  is ", a/b)

# Assignment Operators (=, +=, -=, etc.)

b = 34
b += 1
b -= 4
b *= 2
b /= 17
print(b)

# Comparison Operators (==, >=, <=, >, <, !=, etc.)
c = (4>=7)  #False
c1 = (4<=7)  #true
c3 = (4==7)   #False
c4 = (14!=4)  #False
print(c1,c3,c4)

# Logical Operators (and, or, not)
bool = True
bool2 = False
print("The Valude of bool and bool2",(bool and bool2) )  #and print ture and true * false false then true not to false
print("The Valude of bool and bool2",(bool or bool2) )
print("The Valude of bool and bool2",(bool2) ) 

# type() function and Typecasting

#type function is used to find the data type of a given variable in Python

d = "3344"
print(type(d))
d = int(d) #if you are print (d+6) then use Integer 
print(d+6)

# A number can be converted into a string and vice versa (if possible)

# There are many functions to convert one data type into another.


# Str(31)           # ”31” Integer to string conversion

# int(“32”)       # 32 String to int conversion

# float(32)       #32.0 Integer to float conversion

# a = input(“Enter name”)               #if a is “Vasudev Jaiswal”,
