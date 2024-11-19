import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    
    attempts = 0
    
    # Game loop
    while True:
        # Get user input
        guess = input("Enter your guess: ")
        
        # Ensure the input is an integer
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Increment the attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

# Start the game
guessing_game()
