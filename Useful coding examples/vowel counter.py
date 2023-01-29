string = input("Input a string for the vowels to be counted: ")
string = string.lower()
vowel = ['a', 'e', 'i', 'o', 'u']
count = 0
for letter in string:
    if letter in vowel:
        count += 1
print(f"The number of vowels in the inputted string is {count}")
