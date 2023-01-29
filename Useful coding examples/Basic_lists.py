print("Input 'p' to print the list and 'r' to reverse the list")
names = input("Enter a name for the list: ")
name_list = []
while (names != "p") and (names != "r"):
    name_list.append(names)
    names = input("Enter a name for the list: ")
if names == 'p':
    if name_list == []:
        print("You have not inputted any names yet, please retry.")
    else:
        print(f"Your list of names is {name_list}")

if names == "r":
    if name_list == []:
        print("You have not inputted any names yet, please retry.")
    else:
        name_list.reverse()
        print(f"Your list revsersed is {name_list}")
    

    
