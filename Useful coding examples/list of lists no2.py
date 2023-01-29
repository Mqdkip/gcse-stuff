x=[[1,2,3],[100,200,300],[1,4,9],[4,20,15]]
print(x[2])
#prints the 2nd list in index
print(x[2][1])
#prints the 1st number in index of the 2nd list in index
x[1][0]=10
#changes the 0th number in index of the 1st list in index to 10
x[3][1]=100
#chages the 1st number in index of the 3rd list in index to 100
print(x)
#prints the updated list

for i in x:
    print(i)




