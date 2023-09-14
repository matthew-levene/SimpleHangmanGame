# Hangman Game
#
# Basic hangman game where it takes a single letter as input from the user each round
# Number of rounds is determined by length of word times by 2
# If the letter is not in the list, a piece of the hangman will be drawn
#
# The progress of the hangman will depend on the number of word length
# e.g. the more characters in the word, the longer it takes to draw.
from hangman import Hangman
from generator import generate_word
from matcher import find_matches
from sort import sort_map

if __name__ == '__main__':
    print(
        """
    Welcome to Hangman!
        
    Our hangman friend has committed a crime in a renown capital city.
    In order to save him, you must find out which city he committed the crime in"""
    )

    game_round = 0

    word = generate_word().upper()

    hangman = Hangman(word)

    guess_placeholder = "_"

    user_guessed_word_list = []
    user_guessed_word = ""
    letters_guessed = []

    sorted_word = ""
    correctly_guessed_word_map = {
        x: [] for x in word
    }

    # While the round is less than the word times by 2
    max_rounds = len(word) * 2
    while game_round < max_rounds:

        # Get the input from the user
        letter = input(
            """
    Which letter?: """
        ).upper()

        user_guessed_word += letter

        if not hangman.contains(letter):
            print(
                """
    Letter {} was not found""".format(letter))
        else:
            # For each letter at given index
            for letter_index in range(len(word)):
                # If letter is found at given index and letter has not been previously guessed
                if hangman.contains(letter) and letter not in letters_guessed:
                    letters_guessed.append(letter)
                    # For each index in the word
                    find_matches(letter, word, correctly_guessed_word_map)

            # sort the map
            sorted_list = sort_map(correctly_guessed_word_map)

            if len(sorted_list) > 0:
                print("""
    {}""".format(sorted_list))

            sorted_word = ""
            for letter in sorted_list:
                sorted_word += str(letter)

        if sorted_word == word:
            break
        else:
            game_round += 1

    if hangman.guess(sorted_word):
        print("\nYou saved him! You correctly guessed {}".format(sorted_word))
    else:
        print("\nSorry, you didn't save him!")
        print("The city was: {}, You guessed {}".format(word, user_guessed_word))

