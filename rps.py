import random
import sys

# Initialize scores
wins = 0
losses = 0
ties = 0

print("Welcome to Rock-Paper-Scissors!")
print("Enter (r)ock, (p)aper, (s)cissors, or (q)uit to play.")

while True:
    # Display scores
    print(f"\nWINS: {wins}, LOSSES: {losses}, TIES: {ties}")
    print("What's your choice?")
    player_choice = input().lower()

    # Quit if player enters 'q'
    if player_choice == 'q':
        print("Thanks for playing! Goodbye.")
        sys.exit()

    # Ensure valid input
    if player_choice not in ['r', 'p', 's']:
        print("Invalid choice! Please choose 'r', 'p', 's', or 'q'.")
        continue

    # Display player choice
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    print(f"You chose {choices[player_choice]}...")

    # Computer makes a random choice
    comp_choice = random.choice(['r', 'p', 's'])
    print(f"Computer chose {choices[comp_choice]}.")

    # Determine the result
    if player_choice == comp_choice:
        print("It's a tie!")
        ties += 1
    elif (player_choice == 'r' and comp_choice == 's') or \
         (player_choice == 'p' and comp_choice == 'r') or \
         (player_choice == 's' and comp_choice == 'p'):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1
