import random
questions = 1
score = 0
name = input("What is your name? ")
while questions <= 10:
    questions += 1
    typeof = random.randint(1,3)
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)

    if typeof == 1:
        answer = n1 + n2
        user_answer = int(input(f"What is the answer to {n1} + {n2}? "))
        if user_answer == answer:
            score += 1
            print(f"Correct your score is now {score}")
        
        else:
            print(f"Incorrect the answer was {answer}, your score is {score}.")

    if typeof == 2:
        answer = n1 - n2
        user_answer = int(input(f"What is the answer to {n1} - {n2}? "))
        if user_answer == answer:
            score += 1
            print(f"Correct your score is now {score}")
        
        else:
            print(f"Incorrect the answer was {answer}, your score is {score}.")

    if typeof == 3:
        answer = n1 * n2
        user_answer = int(input(f"What is the answer to {n1} * {n2}? "))
        if user_answer == answer:
            score += 1
            print(f"Correct your score is now {score}")
        else:
            print(f"Incorrect the answer was {answer}, your score is {score}.")

f = open("challenge39.txt", "a")
f.write(f"""
{name}'s score was {score}
""")
f.close()


    


            
                          
                        

    
