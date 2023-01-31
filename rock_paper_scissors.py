import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Papper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in ["rock", "papper", "scissors"]:
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0, papper: 1, scissors: 2


print( " Goodbye ! " )
