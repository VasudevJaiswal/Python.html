# Chapter -5  Dictionary and Sets
# #Dictionary is a collection of @key-value pairs.  [Words and Meanings ]

#Syntaxx 
myDict = {
    "Fast": "In a Quick Manner",
    "Vasudev": "Founder of Jaiswal's Development Studio" ,
    "Marks" : [1,2,4],
    # Nested Dictionary 
    "anotherDict": {
        'vasudev':'developer'
    }

}

print(myDict['Fast'])
print(myDict["Vasudev"])
print(myDict["Marks"])

print(myDict['anotherDict']['vasudev'])

# Properties of Python Dictionaries ? 

# 1. It is unordered
# 2. It is mutable
# 3. It is indexed
# 4. It cannot contain duplicate keys


myDict['Marks'] = [45,58]
print(myDict['Marks'])

# Dictionary Methods ? 
# Consider the following dictionary, 
myDict = {
    "Fast": "In a Quick Manner",
    "Vasudev": "Founder of Jaiswal's Development Studio" ,
    "Marks" : [1,2,4],
    # Nested Dictionary 
    "anotherDict": {
        'vasudev':'developer'
    },
    1:2

}

# items() : returns a list of (key,value) tuple.
print(myDict.items()) # Prints the keys of the dictionary

# keys() : returns a list containing dictionary’s keys.
print(list(myDict.keys()))

# update({“friend”: “Sam”}) : updates the dictionary with supplied key-value pairs.
updatedict = {
    "HANUMAN": "FRIEND"
}
print(myDict.update(updatedict))

# values : #Print the values of lines and dictionary 
print(myDict.values()) #Pritns the keys of the dictionary

# get(“name”) : returns the value of the specified keys (and value is returned e.g., “Harry” is returned here)
print(myDict.get("Vasudev"))
print(myDict['Vasudev'])   #Print the values of Dictionary 



