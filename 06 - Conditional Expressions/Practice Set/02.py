''' Problem 2. Write a program to find the greatest of four numbers entered by 
the user. '''

num1 = int(input("Enter the Number 1: "))
num2 = int(input("Enter the Number 2: "))
num3 = int(input("Enter the Number 3: "))
num4 = int(input("Enter the Number 4: "))

if num1>num4:
    f2 = num1
else:
   f1 = num4

if num2>num3:
    f2 = num2
else:
    f2 = num3

if f1>f2:
    print(str(f1) +" is greatest  ")
else:
    print(str(f2) + " is greatest")
