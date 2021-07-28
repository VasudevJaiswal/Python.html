# Problem 1. Write a program to create a dictionary of Hindi words with values as their English translation. 
# Provide the user with an option to look it up! ?

myDict = {
    "पंखा": "Fan",
    "वास्तु" : "Item",
    " किताब ": "Books"
}
print("Options are", myDict.keys() )
a = input("Enter the Hindi Words is: \n")
print("The meaning of the word is :", myDict[a])

# Problem 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
num1 = input("Enter number 1 \n")
num2 = input("Enter number 2 \n")
num3 = input("Enter number 3 \n")
num4 = input("Enter number 4 \n")
num5 = input("Enter number 5 \n")
num6 = input("Enter number 6 \n")
num7 = input("Enter number 7 \n")
num8 = input("Enter number 8 \n")

S = {num1,num2,num3,num4,num5,num6,num7,num8}  #Reppeation is not allowed
print(S)

# Problem 3. Can we have a set with 18(int) and “18”(str) as a value in it?
s = {18,"18",18.1} 
print(s)

#Problem 4. What will be the length of the following set S:
# S = Set()
# S.add(20)
# S.add(20.0)
# S.add(“20”)

S = {20,20.0,"20"} # in The set 20 and 20.0 is count only one times 
print(S)
print(len(S))

# Problem 5. S = {}, what is the type of S? 
S1 = {}
print(type(S1))  # The type of S1 is Dictionary not the set  TYPE = <class 'dict'>

# Problem 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as values and 
# use keys as their names. Assume that the names are unique.

favLang = {}
a =  input("Enter your favorite language Vasudev")
a1 =  input("Enter your favorite language Aaditya")
a2 =  input("Enter your favorite language Ridhi")
a3 =  input("Enter your favorite language Hanuman")

# This code for End of show 
favLang['Vasudev'] = a
favLang['Aaditya'] = a1
favLang['Ridhi']   = a2
favLang['Hanuman'] = a3
print(favLang)

# Problem 7. If the names of 2 friends are the same; what will happen to the program in Probelm 6.?

favLang['Vasudev'] =  a  #Values can be same but keys not same in python
print(favLang)

# Problem 8. Can you change the values inside a list which is contained in set S
# S = {8, 7, 12, “VasudevJaiswal”, [1, 2]}

# Set ke ander list ko store nhi kiya ja sakta hai 
# Tupple can not be changed

# S = {8, 7, 12, “Vasudev Jaiswal”, [1, 2]}
it is not possible because set {} ke ander list[] nhi ho sakti 

