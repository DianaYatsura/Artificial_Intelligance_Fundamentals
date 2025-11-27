import random

"""
    Selects a random word from a predefined list of words.

    Returns:
    str: A randomly selected word.
    """
hangman_body = {0: (' ',
                    ' ',
                    ' '),
                1: ('o',
                    ' ',
                    ' '),
                2: ('o',
                    '|',
                    ' '),
                3: (' o',
                    '/|',
                    ' '),
                4: (' o',
                    '/|\\',
                    ' '),
                5: (' o',
                    '/|\\',
                    '/ '),
                6: (' o',
                    '/|\\',
                    '/ \\')}



def display_body(wrong_guesses):
    for line in hangman_body[wrong_guesses]:
        print(line)


def select_random_word():
    word_list = ["apple", "banana", "cherry", "dog", "elephant", "flower", "giraffe", "hamburger", "icecream", "jacket"]
    return random.choice(word_list)

"""
    Displays the word with guessed letters filled in and unguessed letters as underscores.

    Args:
    word (str): The target word to guess.
    guessed_letters (list): List of letters guessed by the player.

    Returns:
    str: The word with guessed letters filled in.
    """

def display_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            result += "_"
    return result.strip()

"""
    Executes the Hangman game.

    The player must guess letters in a randomly selected word until they either win or lose.
    """

def hangman_game():
    word_to_guess = select_random_word()
    guessed_letters = []
    max_attempts = 6
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("Try to guess the word. You can make up to 6 wrong guesses.")

    while wrong_guesses < max_attempts:
        print("Word:", display_word(word_to_guess, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{max_attempts}")
        display_body(wrong_guesses)

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            wrong_guesses +=1
            print("Wrong guess.")

    else:
        print(display_body(wrong_guesses))
        print(f"Game over! The word was: {word_to_guess}")

    print("Thank you for playing Hangman!")

hangman_game()
