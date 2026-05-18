import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("I am thinking of a number between 1 and 100.")

# Start the game loop
while True:
    # Get user input and convert to integer
    guess = int(input("Take a guess: "))
    attempts += 1
    
    # Check the user's guess against the secret number
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break  # Exit the loop when the guess is correct