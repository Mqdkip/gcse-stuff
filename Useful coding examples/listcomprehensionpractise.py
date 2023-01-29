#a = [x for x in range (1000) if x % 7 == 0]
#print(a)

#b = [x for x in range (1000) if '3' in str(x)]
#print(b)

#c = [num for num in range(1,1001) if [div for div in range(2,10) if num%div == 0]]
#print(c)

#fish = ("There was a sailor who went to see to sea to see what he could see see see but all that he could see see see was the bottom of the deep blue sea sea sea")
#d = [x for x in fish if x == ' ' ]
#print(len(d))

#fish = ("There was a sailor who went to see to sea to see what he could see see see but all that he could see see see was the bottom of the deep blue sea sea sea")
#vowels = ['a','e','i','o','u']
#e = [x for x in fish if x not in vowels]
#print(e)

fish = ("There was a sailor who went to see to sea to see what he could see see see but all that he could see see see was the bottom of the deep blue sea sea sea")
f = [x for x in fish.split() if len(x) < 4]
print(f)



