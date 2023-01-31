import random

user_wins = 0
computer_wins = 0

options = ["rock", "papper", "scissors"]


while True:
    user_input = input("Type Rock/Papper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0, papper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computore picket", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won")
        user_wins += 1
        continue

    elif user_input == "papper" and computer_pick == "rock":
        print("You won")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "papper":
        print("You won")
        user_wins += 1
            
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computre wons", computer_wins, "times.")
print("Goodbye!")
