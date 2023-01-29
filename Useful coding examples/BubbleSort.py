

def BubbleSort(list1):
        n = len(list1)
        
        for j in range(n-1):
            
            for i in range (0, n-j-1):
                
                if list1[i] > list1[i+1]:
                    list1[i], list1[i+1] = list1[i+1], list1[i]
   
                
list1 = [1,3,6,7,10,9,2,4,8,5]
BubbleSort(list1)


for j in range(len(list1)):
    print(list1[j] )


