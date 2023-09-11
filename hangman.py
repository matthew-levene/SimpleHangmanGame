import random


class Hangman:
    def __init__(self, word):
        self.word = word


def generate_word():
    words = ["London", "Warsaw", "Texas", "Paris", "Amsterdam", "Belgium", "Toronto"]
    return random.choice(words)
