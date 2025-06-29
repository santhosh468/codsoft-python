import random

# Initialize scores
user_score = 0
computer_score = 0

print("="*50)
print("ROCK-PAPER-SCISSORS GAME".center(50))
print("="*50)
print("Rules:")
print("- Rock beats Scissors")
print("- Paper beats Rock")
print("- Scissors beats Paper")
print("- Same choices = Tie")
print("="*50)

while True:
    # User input with validation
    user_choice = input("\nChoose (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please try again.")
        user_choice = input("Choose (rock, paper, scissors): ").lower()
    
    # Computer selection
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    # Display choices
    print(f"\nYour choice: {user_choice.upper()}")
    print(f"Computer's choice: {computer_choice.upper()}")
    
    # Game logic
    if user_choice == computer_choice:
        result = "TIE!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "YOU WIN!"
        user_score += 1
    else:
        result = "COMPUTER WINS!"
        computer_score += 1
    
    # Display result
    print("\n" + "="*50)
    print(f"RESULT: {result}")
    print("="*50)
    print(f"SCORE: You {user_score} - {computer_score} Computer")
    print("="*50)
    
    # Play again prompt
    play_again = input("\nPlay again? (yes/no): ").lower()
    while play_again not in ['yes', 'no']:
        print("Please answer 'yes' or 'no'")
        play_again = input("Play again? (yes/no): ").lower()
    
    if play_again != 'yes':
        print("\nThanks for playing! Final Score:")
        print(f"You {user_score} - {computer_score} Computer")
        print("="*50)
        break