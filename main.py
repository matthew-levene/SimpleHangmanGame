# Hangman Game
#
# Basic hangman game where it takes a single letter as input from the user each round
# Number of rounds is determined by length of word times by 2
# If the letter is not in the list, a piece of the hangman will be drawn
#
# The progress of the hangman will depend on the number of word length
# e.g. the more characters in the word, the longer it takes to draw.
from hangman import Hangman, generate_word

if __name__ == '__main__':
    print(
        """
        Welcome to Hangman!
        
        Our hangman friend has committed a crime in a renown capital city.
        In order to save him, you must find out which city he committed the crime in
        """
    )

    game_round = 0

    word = generate_word()

    hangman = Hangman(word)

    guess_placeholder = "_"
    user_guessed_word = guess_placeholder * len(word)
    letters_guessed = []

    # While the round is less than the word times by 2
    max_round = len(word) * 2
    while game_round < max_round:

        # Get the input from the user
        letter = input("Which letter?: ")

        # For each letter at given index
        for letter_index in range(len(word)):

            # If letter is found at given index, update user guessed word
            if letter in word[letter_index] and letter not in letters_guessed:
                letters_guessed.append(letter)
                # Iterate over letters guessed list, if the letter is not in there, enter the user_guessed_work loop
                # for each index in user_guessed_word find out if letter at word index is same as
                for index in range(len(user_guessed_word)):
                    if letter == word[index]:
                        print("MATCHING LETTER", letter)
                        user_guessed_word = user_guessed_word.replace(guess_placeholder, letter, 1)
                        print("USER GUESSED WORD", user_guessed_word)
                        break

            # print("PRINTING WORD IN FOR: ", word[letter_index])

        game_round += 1

    if user_guessed_word == word:
        print("\nYou saved him! You correctly guessed {}".format(user_guessed_word))
        pass
    else:
        print("\nSorry, you didn't save him!")
        print("The city was: {}. You guessed {}".format(word, user_guessed_word))

