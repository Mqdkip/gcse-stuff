from random import randint 
def flipcoin ():
    number=randint(1,2)
    if number == 1:
        return("heads")

    else:
        return("tails")


def flip_game(n_tries):
    score = 0
    
    for i in range(n_tries):
        print(f"This is turn number {i+1}")
        user = input("heads or tails?").lower()
        coin = flipcoin()

        if coin == user:
            score = score + 1
            print(f"Nice guess your score is now {score}.")

        else:
            print(f"Unlucky guess your score is still {score}.")

    print(f"Your score was {score} in {n_tries} rounds.")

n_tries =  int(input("How many rounds of heads and tails will you be playing?"))
flip_game(n_tries)
    
