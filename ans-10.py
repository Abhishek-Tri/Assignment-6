"""Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""

a=int(input("enter value of a :"))
b=int(input("enter value of b :"))
c=int(input("enter value of c :"))
if a>b:
    if a>c:
        print(a)
elif b>c:
    print(b)
else:
    print(c)
