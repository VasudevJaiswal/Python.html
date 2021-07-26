 # Problem 1. Write a program to store seven fruits in a list entered by the user.

f1 = input("Enter Fruit Number 1 : ")
f2 = input("Enter Fruit Number 2 : ")
f3 = input("Enter Fruit Number 3 : ")
f4= input("Enter Fruit Number 4 :" )
f5 = input("Enter Fruit Number 5 : ")
f6 = input("Enter Fruit Number 6 : ")
f7 = input("Enter Fruit Number 7 : ")
myFruitList = [f1,f2,f3,f4,f5,f6,f7]
print(myFruitList)

# Problem 2. Write a program to accept the marks of 6 students and display them in a sorted manner. 

m1 = int(input("Enter Stundents Number 1 : "))
m2 = int(input("Enter Stundents Number 2 : "))
m3 = int(input("Enter Stundents Number 3 : "))
m4 = int(input("Enter  Stundents Number 4 :"))
m5 = int(input("Enter Students  Number 5 : "))
m6 = int(input("Enter Students  Number 6 : "))

myList = (m1,m2,m3,m4,m5,m6)
myList.sort()
print(myList)

#Problem no.3 Check that a tuple cannot be changed in Python.

a = (2,4,5,3,3)
a[0] =45  #Object error tuple did'nt support Item Assignment

# Problem 4. Write a program to sum a list with 4 numbers.

a = [2,4,2,1]
print(a[0] + a[1] + a[2] + a[3])
print(sum(a))

#Problem 5. Write a program to count the number of zeros in the following tuple:
c3 = [1,2,3,4,5,6,7]
print(c3[0])