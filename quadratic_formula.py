import math
from fractions import Fraction

a = int(input("Enter the coefficients of a: "))
b = int(input("Enter the coefficients of b: "))
c = int(input("Enter the coefficients of c: "))

# findind discriminant
d = b**2-4*a*c 

if d < 0:
    print ("This equation has no real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print ("This equation has one solutions: "), x
else:
    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    
    print ("This equation has two solutions: ", str(Fraction(x1)), " or", str(Fraction(x2)))

