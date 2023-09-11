import random


class Hangman:
    def __init__(self, word):
        self.word = word

    def contains(self, letter):
        return letter in self.word

    def guess(self, guess_word):
        return guess_word in self.word