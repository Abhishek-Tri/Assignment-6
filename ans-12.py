"""Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part"""

c=complex(input("enter a complec number : "))
print(c.real if c.real>c.imag else c.imag)