# Problem 1. Write a Python program to display a user-entered name followed by Good Afternoon using input() function.

name1 = input("Enter your Name:\n")
print("Good After Noon "  +name1)  #Return is Good After noon (name)
 
 # Problem 2. Write a program to fill in a letter template given below with name and date.
Letter = ''' Dear <|NAME|>,
Grreetings from Vasudev Jaiswal . I am happy to tell your about Section

                        You are selected!

                     Date:   <|DATE|> '''


name = input("Enter your Name:\n")
date = input("Enter DATE: \n ")
Letter = Letter.replace("<|NAME|>",name)
Letter = Letter.replace("<|DATE|>",date)
print(Letter)

# Problem 3. Write a program to detect double spaces in a string.

st = "This is a string with double     Spaces"
doubleSpaces = st.find("   ")
pritn(doubleSpaces)


# Problem 4. Replace the double spaces from problem 3 with single spaces.

st = st.replace(" "," ")
print(st)

# Problem 5. Write a program to format the following letter using escape sequence characters.

letter = "Dear Vasudev Jaiswal you are a great Developer in the world \n Thanks for visiting "
print(letter)