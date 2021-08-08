'''Problem 1. 
Write a program to print the multiplication table of a given number using for loop.'''

num = int(input("Enter the Number : "))
for i in range(1,11):
    # print(str(i) + "X" +str(i) + "=" +str(i*num))
    print(f"{num}X{i}={num*i}")



''' PS C:\Users\Vasudev Jaiswal\Documents\Python> & "C:/Users/Vasudev Jaiswal/AppData/Local/Programs/Python/Python39/python.exe" "c:/Users/Vasudev Jaiswal/Documents/Python/07 - Loops/Practice sets/02.py"
# @output of Python code: 
Enter the Number : 2
2X1=2
2X2=4
2X3=6
2X4=8
2X5=10
2X6=12
2X7=14
2X8=16
2X9=18
2X10=20  '''