
def bubblesort(list2):
    
    length = len(list2)
    

    swapped = 1

    while swapped == 1:
        swapped = 0
        for i in range (1,length):

            if list2[i-1] > list2[i]:
                temp = list2[i-1]

                list2[i-1] = list2[i]
                list2[i] = temp

                swapped = 1

                print(list2)

list2 = [1,3,6,7,10,9,2,4,8,5]
bubblesort(list2)
