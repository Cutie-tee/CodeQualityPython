import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome people!")
print("I'm thinking of a number between 1 and 100.")

# Initialize the guess count
guess_count = 0

while True:
    # Get the player's guess
    guess = input("Enter your guess: ")
    
    # Validate the input
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    guess_count += 1
    
    # Check the guess
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {guess_count} tries!")
        break

print("Thanks for playing!")