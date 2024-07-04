# # Using a for loop to print the statement five times
# # print(f"\n\tSPACE HOLDER")     """"""
# print(f"\n\tSPACE HOLDER") 
# # print(f"\n\tSPACE HOLDER")     """"""
# print(f"\n\tSPACE HOLDER") 


def convert_to_phonetic(word):
    letters_to_words = {
        'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',
        'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett',
        'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar',
        'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
        'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray',
        'y': 'Yankee', 'z': 'Zulu',
    }
import random

for _ in range(5):
    print(f"\n\tSPACE HOLDER")

# print simple image
def create_simple_image():
    # Define the dimensions of the image grid
    width = 5
    height = 5
    
    # Create an empty grid represented by a list of dictionaries
    image = []
    for _ in range(height):
        row = {'.'}, width  # Initialize each row with dots
        image.append(row)
    
    # Print the image
    for row in image:
        print(' ', row)

# Call the function to create and display the image
create_simple_image()



# begin guessing game
def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have picked a number between 1 and 100. Can you guess what it is?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guessing_game()
    else:
        print("Thanks for playing!")

# Start the game
guessing_game()
