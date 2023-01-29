print("Find the number of digits in an integer\n")
d = 1
number = int(input("Enter an integer: "))
temp = number
while True:
    temp = temp / 10
    d = d + 1
    if temp < 10:
        break
print(f"Number of decimal places in {number} is {d}")

