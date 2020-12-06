# snake water gun game 
import random
lst = ['s','w','g']
chance = 5
no_of_chance = 0
computer_point = 0
your_point = 0
print("SNAKE WATER GUN GAME.")
print("s for Snake\nw for Water\ng for Gun")
print("You have only 5 chance to win this game. ")

while no_of_chance < chance:
    user = input("Enter what you choose: ")
    computer = random.choice(lst)
    
    if user == computer:
        print("Tie both 0 point to each \n")
    
    # if user enter s
    elif user == "s" and computer == "g":
        computer_point = computer_point + 1
        print(f"Your guess {user} and computer guess is {computer}")
        print("Computer wins this point\n")
        print(f"Computer point is {computer_point} and Your point is {your_point}. ")
    elif user == "s" and computer == "w":
        your_point = your_point + 1
        print(f"Your guess is {user} and Computer guess is {computer}.")
        print("You win this point.\n")
        print(f"Computer point is {computer_point} and Your point is {your_point}.")
    # if user enter w
    elif user == "w" and computer == "s":
            computer_point = computer_point + 1
            print(f"Your guess {user} and computer guess is {computer}")
            print("Computer wins this point\n")
            print(f"Computer point is {computer_point} and Your point is {your_point}. ")
    elif user == "w" and computer == "g":
        your_point = your_point + 1
        print(f"Your guess is {user} and Computer guess is {computer}.")
        print("You win this point.\n")
        print(f"Computer point is {computer_point} and Your point is {your_point}.")
    # if user enter g
    elif user == "g" and computer == "w":
            computer_point = computer_point + 1
            print(f"Your guess {user} and computer guess is {computer}")
            print("Computer wins this point\n")
            print(f"Computer point is {computer_point} and Your point is {your_point}. ")
    elif user == "g" and computer == "s":
        your_point = your_point + 1
        print(f"Your guess is {user} and Computer guess is {computer}.")
        print("You win this point.\n")
        print(f"Computer point is {computer_point} and Your point is {your_point}.")
    else:
        print("You have input wrong")
    no_of_chance += 1
    print(f"{chance - no_of_chance} chances  are left out of {chance} chances")


print(f"-->Your point is {your_point} and computer point is {computer_point}")
if computer_point == your_point:
    print("Tie")
elif your_point > computer_point:
    print("-->You wins,Computer loose")
else:
    print("-->Computer wins You loose")

print("Game Over")     
    