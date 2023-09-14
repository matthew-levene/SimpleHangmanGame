import random


def generate_word():
    words = [
        ("London", "home to Big Ben"),
        ("Texas", "popular american city known for BBQ and steaks"),
        ("Paris", "referred to as the city of love"),
        ("Amsterdam", "known for its historic canals"),
        ("Belgium", "known for its chocolate")
    ]
    return random.choice(words)
