print("Input 'a' to get the average and 'q' to quit the program")
number = input("Enter a number: ")
nums = []
while (number != 'a') and (number != 'q') and (number != 'm'):
    nums.append(float(number))
    number = input("Enter a number: ")
if number == 'a':
    if nums == []:
            print("You have not inputted any numbers yet, please retry.")
    else:
        total = sum(nums)
        length = len(nums)
        average = total/length
        print (f"average: {average}")
else:
    print ('You have quit the program')



    
