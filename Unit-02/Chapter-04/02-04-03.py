import random

def play_game():
    print("=== Welcome to the Number Guessing Game! ===")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    # Game loop
    while not guessed_correctly:
        try:
            # Get player guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
                guessed_correctly = True
                
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")

# Run the game
play_game()
