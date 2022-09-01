"""Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""

print("enter value of a,b,c of quadratic equation : ",end='')
a,b,c=int(input()),int(input()),int(input()) 
d=b**2-4*a*c
if d>0:
    print("real and distinct roots")
elif d==0:
    print("real and equal roots")
else:
    print("imaginary roots")           