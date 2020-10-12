#!/usr/local/bin/python3
from random import choice

# Global constants
NUM_TURNS = 8
WORDS_FILE = "words.txt"


def check_victory(letters_guessed, letters_to_guess):
    """
    1. Loop through all of the letters in `letters_to_guess`.
    2. For each letter:
        2a. If the letter is not an element of `letters_guessed`, return False.
    3. Return True.
    """
    for letter in letters_to_guess:
        if letter not in letters_guessed:
            return False

    # assert every element of letters_to_guess is an element of letters_guessed
    return True

    """
    # check_victory using subset operations
    return letters_to_guess <= letters_guessed
    """


def get_guess(letters_guessed):
    """
    1. Set up an input validation loop (use `while True`).
    2. Get user input and convert it to lowercase.
        2a. If user input is not a letter, tell the user their guess is invalid.
        2b. If user input is already an element of `letters_guessed`, tell the user they've already guessed that letter.
        2c. If user guessed more than one letter, let them know they may only guess a single letter at a time.
        2d. Otherwise, return the user guess.
    """
    while True:
        user_input = input("Enter a letter to guess: ").lower()

        if not user_input.isalpha():
            print("You may only guess letters!")

        elif user_input in letters_guessed:
            print("You've already guessed that!")
            print(f"As a reminder, you've guessed {', '.join(letters_guessed)}.")

        elif len(user_input) != 1:
            print("You may only guess one letter at a time!")

        else:
            return user_input


def show_guessed_so_far(word_to_guess, letters_to_guess, letters_guessed):
    """
    1. Create an output string by assigning from word_to_guess.
    2. For every letter in letters_to_guess:
        2a. If the letter is not an element in letters_guessed, replace its occurrences in the output string with '_'.
        2b. Otherwise, continue at the top of loop.
    3. Return the output string.
    """
    occulted_word = " ".join(word_to_guess)

    for letter in letters_to_guess:
        if letter not in letters_guessed:  # if this letter has not been guessed by the player
            occulted_word = occulted_word.replace(letter, "_")

    print(occulted_word)    


def play_game(word_to_guess):
    """
    1. Initialize the game state based on word_to_guess.
        1a. Create a set of letters that need to be guessed.
        1b. Create an empty set of letters that have been guessed.
        1c. Set the number of guesses used to 0.
    
    2. Print the length of the word to be guessed.
    
    3. While the  number of guesses used is less than `NUM_TURNS`:
        3a. Show the user what they've guessed so far.
        3b. Get a new user guess
        3c. Check whether the new user guess is an element of word to be guessed:
            3ci. if yes, let the user know that they guessed correctly
            3cii. otherwise, let the user know they guessed incorrectly and add 1 to number of guesses used
    
        3d. Check if the user has guessed all the letters in the word.
            3di. If yes, print a victory message.
            3dii. If no, continue at the top of the loop.

    4. Print a message indicating the user lost and revealing the word.
    5. Exit from the function (no return value).
    """
    letters_to_guess = set(word_to_guess)
    letters_guessed = set()
    guesses_used = 0

    print(f"Your word has {len(word_to_guess)} letters.")

    while guesses_used < NUM_TURNS:
        show_guessed_so_far(word_to_guess, letters_to_guess, letters_guessed)

        new_guess = get_guess(letters_guessed)
        letters_guessed.add(new_guess)

        if new_guess in letters_to_guess:
            print("Correct!")

        else:
            print("Incorrect!")
            guesses_used += 1

        user_has_won = check_victory(letters_guessed, letters_to_guess)

        if user_has_won:
            print("Congratulations, you win!")
            print(f"You finished in {guesses_used} turns!")
            return

    # assert guesses_used == NUM_TURNS
    print("You lose!")
    print(f"Your word was {word_to_guess}")
    return


def read_words(filename):
    """
    1. Open the file for reading.
    2. Read in all of the contents of the file as a string.
    3. Use the .split() method to break the file contents at newline characters.
    4. return the result of step 3.
    """
    with open(filename) as wordsfile:
        words = wordsfile.read().lower()

    return words.split()


def filter_by_difficulty(words, desired_difficulty):
    """
    HINT: LIST COMPREHENSIONS WOULD WORK GREAT HERE.

    1. Check value of `desired_difficulty`:
        1a. if 'easy', filter from `words` all words whose length is less than 4 or greater than 6.
        1b. if 'normal', filter from `words` all words whose length is less than 6 or greater than 8.
        1c. if 'hard', filter from `words` all words whose length is less than 8.
    2. Return the list obtained in step 1.
    """
    if desired_difficulty == 'easy':
        return [w for w in words if 4 <= len(w) <= 6]

    elif desired_difficulty == 'normal':
        return [w for w in words if 6 <= len(w) <= 8]

    else:
        return [w for w in words if 8 < len(w)]


def get_word_to_guess(desired_difficulty):
    """"
    1. Read all words from words.txt
    2. 
    3. Return a word at random from the list of words obtained in step 2.  
    """
    words = read_words(WORDS_FILE)
    filtered = filter_by_difficulty(words, desired_difficulty)
    return choice(filtered)


def get_user_difficulty():
    """
    1. Setup an input validation loop.
    2. While the user input is not valid:
        2a. ask for user input
        2b. if the user input is not 'easy', 'normal', or 'hard', alert the user that the input is invalid
        2c. otherwise, return the user input (normalize to lowercase).
    """
    while True:
        user_input = input("Select a difficulty ('easy', 'normal', 'hard'): ").lower()

        if user_input in {'easy', 'normal', 'hard'}:
            return user_input

        print("Invalid difficulty. Valid values are 'easy', 'normal', and 'hard'.")


def prompt_play_again():
    """
    1. Set up an input validation loop.
    2. Get user input.
        2a. If the input is 'yes', return `True`.
        2b. If the input is 'no', return `False`.
        2c. Otherwise, inform the user that the option is invalid.
    """
    while True:
        user_selection = input("Play again? ('yes'/'no'): ").lower()

        if user_selection == 'yes':
            return True

        elif user_selection == 'no':
            return False

        print("Invalid selection. Enter 'yes' or 'no'.")


def run_game_loop():
    """
    1. Get desired user difficulty (easy, normal, hard).
    2. Get a word for the player to guess.
    3. Play the game.
    4. Ask if the user wants to play again.
        4a. If they do, play the game again.
        4b. Otherwise, exit the prorgram.
    """
    desired_difficulty = get_user_difficulty()
    word_to_guess = get_word_to_guess(desired_difficulty)
    play_game(word_to_guess)

    play_again = prompt_play_again()

    if play_again:
        run_game_loop()

    else:
        print("Goodbye!")
        exit(0)


def main():
    """
    Run the game loop.
    """
    print("Welcome to mystery word!")
    run_game_loop()


if __name__ == "__main__":
    main()