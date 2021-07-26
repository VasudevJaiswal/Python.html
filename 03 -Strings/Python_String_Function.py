# String Functions ?
# Some of the most used functions to perform operations on or manipulate strings are:


# String Fuctions : Examples

story = '''once upon a time there was a Developer named Vasudev Jaiswal 
who uploaded  python course with notes on github'''
print(story[0:5])


# 1. len() function : It returns the length of the string.

print(len(story))  #Character of the story string. Function the --- return is 111 character


# 2. endswith(“rry”) : This function tells whether the variable string ends with the string “rry” or not. If string is “harry”, it returns for “rry” since harry ends with rry.

print(story.endswith("github"))  #Story End with github so that ---  return is true 


# 3. count(“c”) : It counts the total number of occurrences of any character.

print(story.count("a"))    #In the Stroy Count of a word is -- return is 8 
print(story.count("notes"))   # return is = 1


# 4. capitalize() : This function capitalizes the first character of a given string.

print(story.capitalize())


# 5. find(word) : This function finds a word and returns the index of first occurrence of that word in the string.

print(story.find("Vasudev"))  # Vasudev is the found the story in 45 Character 
print(story.find("upon"))    #5 Character 


# 6. replace(oldword, newword) : This function replaces the old word with the new word in the entire string.

print(story.replace("Vasudev", "Vasu dev Python"))  # Replace the Vasudev with the Vasu dev Python 

