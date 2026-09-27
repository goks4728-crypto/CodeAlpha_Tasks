import random

def play_hangman():
    # 5 predefined words
    words = ["python", "hangman", "program", "code", "developer"]
    
    # Randomly select a word
    secret_word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Limit incorrect guesses to 6

    print("Welcome to Hangman!")

    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Build the current state of the word (e.g., "p y _ h o n")[cite: 1]
        display_word = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print("\nWord: " + " ".join(display_word))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print("Guessed letters:", " ".join(guessed_letters) if guessed_letters else "None")

        # Check if the player has guessed all letters
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            break

        # Get user input[cite: 1]
        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        # Check if letter is in secret word[cite: 1]
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    # End game condition for losing
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame Over! The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()