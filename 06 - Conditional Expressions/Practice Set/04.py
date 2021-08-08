''' Problem 4. A spam comment is defined as a text containing the following keywords:
“make a lot of money”, “buy now”, “subscribe this”, “click this”. 
Write a program to detect these spams.'''

#Spam detecter for machine learnings

comment = input("Enter the text")
if("Make a Lot of money " in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("Click This"):
    spam = True
elif("Subscribe Now"):
    spam = True
else:
    spam = False

if(spam):
    print("Enter text is spam")
else:
    print("This text is not spam")


