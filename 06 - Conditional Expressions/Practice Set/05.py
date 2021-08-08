''' Problem 5. Write a program that finds out whether 
a given name is present in a list or not.'''

# Name search genrator using the Python 

names = ["Vasudev","Ridhi","hritik","Hanuman", "Gaurav"]
name = input("Enter the Name : ")
if name in names:
    print("Your name is in the list")
else:
    print("Your name is not in the list")