import random

def play_hangman():
    # 1. Predefined list of 5 words
    word_list = ["python", "coding", "program", "project", "intern"]
    secret_word = random.choice(word_list)
    
    # Track game states
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    # 2. Visual "Cartoon" stages using ASCII character art (0 to 6 mistakes)
    hangman_stages = [
        r"""
           --------
           |      |
           |
           |
           |
           |
        --------
        """,
        r"""
           --------
           |      |
           |      O
           |
           |
           |
        --------
        """,
        r"""
           --------
           |      |
           |      O
           |      |
           |      |
           |
        --------
        """,
        r"""
           --------
           |      |
           |      O
           |     /|
           |      |
           |
        --------
        """,
        r"""
           --------
           |      |
           |      O
           |     /|\
           |      |
           |
        --------
        """,
        r"""
           --------
           |      |
           |      O
           |     /|\
           |      |
           |     /
        --------
        """,
        r"""
           --------
           |      |
           |      O
           |     /|\
           |      |
           |     / \
        --------
        """
    ]

    print("=========================================")
    print("      WELCOME TO THE HANGMAN GAME        ")
    print("=========================================")
    print("Rules: Guess the secret word one letter at a time.")
    print(f"You can make up to {max_incorrect} incorrect guesses before losing.")
    
    # Main game loop
    while incorrect_guesses < max_incorrect:
        # Print the current stick figure stage
        print(hangman_stages[incorrect_guesses])
        
        # Build and display the current hidden word progress
        displayed_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word.append(letter)
            else:
                displayed_word.append("_")
        
        print("Word: " + " ".join(displayed_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        # Check if the player won
        if "_" not in displayed_word:
            print("\n🎉 Congratulations! You guessed the word correctly! 🎉")
            break

        # Get player input
        guess = input("Guess a letter: ").lower().strip()

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter!")
            continue

        # Process the valid guess
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Oops! '{guess}' is not in the word.")

    # Game over condition
    if incorrect_guesses == max_incorrect:
        # Print the final complete hangman figure
        print(hangman_stages[incorrect_guesses])
        print("=========================================")
        print("💀 Game Over! You ran out of guesses.")
        print(f"The correct word was: '{secret_word}'")
        print("=========================================")

if __name__ == "__main__":
    play_hangman()