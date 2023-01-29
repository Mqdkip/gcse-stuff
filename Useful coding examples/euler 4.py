#euler 4

newlist = []
for i in range(100,1000):
    for x in range(100,1000):
        number = x * i
        if str(number) == str(number)[::-1]:
            newlist.append(number)
print(max(newlist))
            
