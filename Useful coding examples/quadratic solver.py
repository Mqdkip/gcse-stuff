#quadratic solver
from math import sqrt


print("A quadratic has the form 'ax^2 + bx + c'.")
print("To run the amount of possible solutions type ('solutions(a,b,c)')")

def solutions(a,b,c):
    if a == 0:
        print("Invalid input for 'a' ")

    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-sqrt(b**2-4*a*c))/(2*a)
    print(f"The first solution is {x1}")
    print(f"The second solution is {x2}")
    
    delta = b*b - 4*a*c
    if delta == 0:
        return 1

    elif delta > 0:
        return 2

    else:
        return 0


   
