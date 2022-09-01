"""Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same."""

a=int(input("enter first number :"))
b=int(input("enter second number :"))
if a>b:
    print("a is greater")
elif b>a:
    print("b is greater")
else:
    print("a & b are equal")        
