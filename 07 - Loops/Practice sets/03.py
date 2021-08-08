'''Problem 2. Write a program to greet all the person names 
stored in a list l1 and which starts with S.'''


l1 = ["Vasudev","Vivek","Vikas","Vinod","Hanuman","Aaditya"]
for name in l1:
    if name.startswith("V"):
        print("Hello"  +  name)
        
