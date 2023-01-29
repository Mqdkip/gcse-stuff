# Loop through these numbers and find the total of all the odd numbers and the total of all the even numbers.

numbers =[4, 8, 5, 7, 13, 76, 34, 52]
toteven = 0
totodd = 0

for i in numbers:
    if (i%2 == 0):
        toteven =  toteven + i

    else:
        totodd = totodd + i 
        
print(f"The total of odd numbers is {totodd}")
print(f"The total of odd numbers is {toteven}")    
    
