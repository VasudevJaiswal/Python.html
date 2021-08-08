


'''Problem 4. Write a program to find whether a given number is prime or not.'''




num = int(input("Enter the number : "))
prime = True
for i in range(2,num):
    if(num%1 == 0):
        prime = False
        break
if prime:
    print("This is a P6rime Number")
else:
    print("This Number is Not  Prime Number")

        