import random
player = 0
comp = 0
def playeritem():
    item = input("Choose Rock, Paper or Scissors: ")
    if item in ["Rock", "rock", "r", "R"]:
        item = "r"
    elif item in ["Paper", "paper", "p", "P"]:
        item = "p"
    elif item in ["Scissors", "scissors", "s", "S"]:
        item = "s"
    else:
        print("That's not vaild play,check your spelling!")
        playeritem()
    return item

def compitem():
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "r"
    elif computer == 2:
        computer = "p"
    else:
        computer = "s"
    return computer

name=input("Hello,What is your name")
print("Hi",name)
print("Are you ready to play scissors paper rock game?")
print("This game is very easy you just have to select the following...")
print(">>> scissors ")
print(">>> paper ")
print(">>> rock ")
T=input("Ready?Press T to start the game...")
while T:
    player_c=playeritem()
    comp_c=compitem()
    
    if player_c == "r":
        if comp_c == "r":
            print("You chose rock. The computer chose rock. You tied.")
        
        elif comp_c == "p":
            print("You chose rock. The computer chose paper. You lose.")
            comp += 1
            
        elif comp_c == "s":
            print("You chose rock. The computer chose scissors. You win.")
            player += 1

    elif player_c == "p":
        if comp_c== "r":
            print("You chose paper. The computer chose rock. You win.")
            player += 1
        
        elif comp_c == "p":
            print("You chose paper. The computer chose paper. You tied.")
            
            
        elif comp_c == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            comp += 1

    elif player_c == "s":
        if comp_c == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            comp += 1
        
        elif comp_c == "p":
            print("You chose scissors. The computer chose paper. You win.")
            player += 1
            
        elif comp_c == "s":
            print("You chose scissors. The computer chose scissors. You tied.")

    print("")    
    print("You: " + str(player))
    print("Computer : " +str(comp))
    print("")

    user_choice = input("Do you want to play again? (yes/no)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break

    


       
    
        

    

