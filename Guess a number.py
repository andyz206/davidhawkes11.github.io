import random

number = random.randint(1,10)
turns = 0


def game():
    q = int(input("Guess a number between 1 to 10, please."))
    if q < number:
        print("The number that you guessed was too small,please try again.")
        turns =+1
        game()
    elif q > number:
        print("The number that you guessed was too big,please try again.")
        turns =+1
        game()
    elif q == number:
        print("Congratulations!!! You Won!")
    else:
        print("Check your spelling please!")
        game()

f = game()

    






        

        
        
    
        
    
        
    
