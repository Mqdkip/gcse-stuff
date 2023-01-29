def order():
    order1 = ["Tomato","Cheese"]
    
    extras1 = ["Pepperoni", "chicken", "extra_cheese", "mushrooms", "spinach", "olives"]
    
    size = input("What size pizza do you want the pizza? [Small, Medium, or Large]")
    
    size.lower()

    while (size != "small") and (size != "medium") and (size != "large"):
        print("You have entered an invalid size")
        size = input("What size pizza do you want the pizza? [Small, Medium, or Large]")
        
    
    order1.append(size)


    
    base = input("Should the base be thick or thin?")

    base.lower()

    while (base != "thick") and (base != "thin"):
        print("You have entered an invalid thickness")
        base = input("Should the base be thick or thin?")
        
    order1.append(base)    
        

    
    
    standards = str(input("Do you want to remove cheese, tomato or both or none?"))
    
    standards.lower()
    
    if standards == "tomato":
        order1.pop(0)
    elif standards == "cheese":
        order1.pop(1)
    elif standards == "both":
        order1.pop(0)
        order1.pop(0)
    else:
        pass
    
    

    
    print(extras1)
    for i in range(1,4):
        extras = input(f"What extra toppings do you want?")
        order1.append(extras)

    print(order1)


    confirm = input("Are you happy with your order?")
    confirm.lower()
    while confirm == "no":
            order()
    elif confirm == "yes":
        pass

    else:
        pass


order()






    
