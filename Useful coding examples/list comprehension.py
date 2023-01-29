#list comprehension

cubes = [i**3 for i in range (1,101)]
print(cubes)


animals = ["dog", "cat", "rat", "giraffe", "gorilla"]
length = [len(i) for i in animals]
print(length)
newlist = []
for i in range(len(animals)):
    if len(animals[i]) > 5:
        newlist.append(animals[i])
print(newlist)


