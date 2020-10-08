from random import choice

# Global constants
NUM_TURNS = 8
WORDS_FILE = "words.txt"


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
    pass


def filtered_by_difficulty(words, desired_difficulty):
    """
    HINT: LIST COMPREHENSIONS WOULD WORK GREAT HERE.

    1. Check value of `desired_difficulty`:
        1a. if 'easy', filter from `words` all words whose length is less than 4 or greater than 6.
        1b. if 'normal', filter from `words` all words whose length is less than 6 or greater than 8.
        1c. if 'hard', filter from `words` all words whose length is less than 8.
    2. Return the list obtained in step 1.
    """
    pass


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
    pass


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