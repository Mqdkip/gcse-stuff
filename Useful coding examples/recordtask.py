my_group = [["001","Leigh","Rosie","3SH","F",10,True],["003","Walliams","George","3SH","M",4,True],["012","Hey","Rebecca","3TS","F",12,False],["018","Hume","Ken","3HJ","M",0,False],["031","Heer","Parul","3TS","F",8,True]]

for i in my_group:
    print("Pupils surnames",i[1])

for i in my_group:
    print("Pupils first name",i[2])

for i in my_group:
    print("Pupils gender:",i[4])

my_group.append(["070","Groves","Josh","3PP","M",8,True])
my_group[3].pop()

print(my_group)
