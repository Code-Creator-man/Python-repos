import random

print("Do you wanna play Rock, Paper, or Scissors?")
my_choice = input("Me: ").lower()
choices = ('rock', 'paper', 'scissors')

if my_choice not in choices:
    print("You might have typed it wrong!")
else:
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # Mapping each choice to what it beats
    wins = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    if my_choice == computer_choice:
        print("It's a tie!")
    elif wins[my_choice] == computer_choice:
        print("You won!")
    else:
        print("I won!")

