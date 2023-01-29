def getarea (length,height):
    area = length * height * 0.5
    return area

height = int(input("What is the height of the triangle?"))
length = int(input("What is the base of the triangle?"))
my_area = getarea(length,height)
print(f"The area is {my_area}")

def getangle (angle1, angle2):
    angle3 = 180 - (angle1 + angle2)
    return angle3

angle1 = int(input("What is the first angle of the triangle?"))
angle2 = int(input("What is the second angle of the triangle?"))

my_angle = getangle (angle1, angle2)
print(f"The area is {my_angle}")


def isEquilateral(side1,side2,side3):
    equilateral = (side1 == side2 == side3)
    return bool(equilateral)
        
side1 = int(input("What is the first sidelength of the triangle?"))
side2 = int(input("What is the second sidelength of the triangle?"))
side3 = int(input("What is the third sidelength of the triangle?"))
my_equilateral = isEquilateral(side1,side2,side3)
if my_equilateral == True:
    print(f"The triangle is equilateral")
else:
    print(f"The triangle is not equilateral")


    





