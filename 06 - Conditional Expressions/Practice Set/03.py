'''Problem 3. Write a program to find out whether a student is pass or fail if it 
requires a total of 40% and at least 33% in each subject to pass. 
Assume 3 subjects and take marks as an input from the user. '''

sub1 = int(input("Enter first Subject marks : "))
sub2 = int(input("Enter Seconed Subject marks : "))
sub3 = int(input("Enter Third Subject marks : "))

if(sub1>33 or sub2>33 or sub3>33):
    print("You are Fail because you have less than 33% in one of the subject ")

if(sub1+sub2+sub3)/3 <40:
    print("You are fail due to total percentage less than 40 %")
else:
    print("Congratulations: You are Passed in Exam ")
