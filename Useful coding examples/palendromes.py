def palendromic_number(number):

   while True:
       number += 1
       if str(number) == str(number)[::-1]:
           print(number)
           break


number = int(input("input a number "))
palendromic_number(number)
