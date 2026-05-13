# Juego del ahorcado
import random

WORDS = [
    "python", "programming", "computer", "algorithm", "function",
    "variable", "dictionary", "recursion", "iteration", "exception"
]

def choose_word():
    return random.choice(WORDS)

def display_word(word, guessed_letters):
    return ' '.join(c if c in guessed_letters else '_' for c in word)

def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """
    ]
    return stages[attempts]

def play():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = set()
    max_attempts = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.\n")

    while len(wrong_guesses) < max_attempts:
        print(display_hangman(len(wrong_guesses)))
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'None'}")
        print(f"Attempts left: {max_attempts - len(wrong_guesses)}\n")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter.\n")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"'{guess}' is in the word!\n")
        else:
            wrong_guesses.add(guess)
            print(f"'{guess}' is not in the word.\n")

        if all(c in guessed_letters for c in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            return

    print(display_hangman(max_attempts))
    print(f"\nGame over! The word was: {word}")

play()
