#Write a python script to check whether a given year is a leap year or not.
year=int(input("enter a year : "))
if year%400==0:
    print("leap year")
elif year%100==0:
    print("Not leap year")
elif year%4==0:
    print("leap year") 
else:
    print("Not leap year")    