'''Problem 2. Write a program to greet all the person names 
stored in a list l1 and which starts with S.'''


l1 = ["Vasudev","Vivek","Vikas","Vinod","Hanuman","Aaditya"]
for name in l1:
    if name.startswith("V"):
        print("Hello"  +  name)
        

'''Result is

PS C:\Users\Vasudev Jaiswal\Documents\Python> & "C:/Users/Vasudev Jaiswal/AppData/Local/Programs/Python/Python39/python.exe" "c:/Users/Vasudev Jaiswal/Documents/Python/07 - Loops/Practice sets/03.py"


HelloVasudev
HelloVivek
HelloVikas
HelloVinod
'''