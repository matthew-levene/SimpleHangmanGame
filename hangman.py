

class Hangman:
    def __init__(self, word):
        self.word = word
        self.num_wrong_guesses = 0

    def contains(self, letter):
        return letter in self.word

    def guess(self, guess_word):
        return guess_word == self.word


    def draw_left_right_leg(self):
        print("""
        |            / \\""", end="")
    def draw_left_leg(self):
        print("""
        |            /""", end="")
    def draw_left_right_arm(self):
        print("""
        |             |
        |            /|\\
        |             |""", end="")

    def draw_left_arm(self):
        print("""
        |             |
        |            /|
        |             |""", end="")
    def draw_body(self):
        print("""
        |             |
        |             |
        |             |""", end="")

    def draw_neck(self):
        print("""
        |            \/""", end="")


    def draw_head(self):
        print("""
        |         /\\/\\/\\/\\
        |         | x  x |
        |        (    ^   )
        |         ---  ---""", end="")
    def draw_arch(self):
        print("""
          ----------
         /           \\
        /             |""", end="")

    def draw_post(self):

        print("""
        |
        |""", end="")
    def draw_gallow_stand(self):
        print("""
        ________________\n""", end="")


    def draw_hangman(self):
        self.num_wrong_guesses += 1
        if self.num_wrong_guesses == 1:
            self.draw_gallow_stand()
        elif self.num_wrong_guesses == 2:
            self.draw_post()
            self.draw_gallow_stand()
        elif self.num_wrong_guesses == 3:
            self.draw_arch()
            self.draw_post()
            self.draw_gallow_stand()
        elif self.num_wrong_guesses == 4:
            self.draw_arch()
            self.draw_head()
            self.draw_post()
            self.draw_gallow_stand()
        elif self.num_wrong_guesses == 5:
            self.draw_arch()
            self.draw_head()
            self.draw_neck()
            self.draw_post()
            self.draw_gallow_stand()
        elif self.num_wrong_guesses == 6:
            self.draw_arch()
            self.draw_head()
            self.draw_neck()
            self.draw_body()
            self.draw_post()
            self.draw_gallow_stand()
        elif self.num_wrong_guesses == 7:
            self.draw_arch()
            self.draw_head()
            self.draw_neck()
            self.draw_left_arm()
            self.draw_post()
            self.draw_gallow_stand()
        elif self.num_wrong_guesses == 8:
            self.draw_arch()
            self.draw_head()
            self.draw_neck()
            self.draw_left_right_arm()
            self.draw_post()
            self.draw_gallow_stand()
        elif self.num_wrong_guesses == 9:
            self.draw_arch()
            self.draw_head()
            self.draw_neck()
            self.draw_left_right_arm()
            self.draw_left_leg()
            self.draw_post()
            self.draw_gallow_stand()
        elif self.num_wrong_guesses == 10:
            self.draw_arch()
            self.draw_head()
            self.draw_neck()
            self.draw_left_right_arm()
            self.draw_left_right_leg()
            self.draw_post()
            self.draw_gallow_stand()

        return self.hangman_complete()

    def hangman_complete(self):
        return self.num_wrong_guesses == 10





        # Bottom Frame, Post, Arch, Noose, Head, Body, L.Arm, R.Arm, L.Leg, R.Leg == 10



