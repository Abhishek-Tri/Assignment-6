#Write a python script to check whether a given number is a three digit number or not.
c=0
n=eval(input("enter a number :"))
while n>1:
    n=n/10
    c=c+1
if c==3:
    print("3 Digit Number")
else:
    print("Non 3 digit number")        
