import random


def play_mad():
    # This is a comment! Use a hash to mark a line as a comment
    # First we create the body of the MadLib
    story = "Today I ate %s %s."
    # Then we ask the user to input the name of a fruit and store it in variable "fruit"
    fruit = input("Please enter the name of some fruit")
    # Here we examine the first letter of whatever the user entered. The easy Python way to do this is
    # with indexing. To pull a single letter from a string, add brackets after the string and enter
    # position of the character you want. Indexes start from 0, so fruit[0] will pull the first letter of the fruit
    # variable.
    #
    # This structure below is called a "conditional." It's also known as an if/then condition. The "in" command
    # checks to see if one thing is inside another thing. Here, we are checking if the first letter of the fruit
    # variable is inside the string "aeiou" (our string of vowels). If it is, then our a_or_an variable is set to "an"
    # otherwise, our a_or_an variable is set to "a".
    if fruit[0] in ("aeiou"):
        a_or_an = "an"
    else:
        a_or_an = "a"
    # Finally, our story is printed, with the a_or_an variable in its place and the fruit variable in its place, using
    # string substitution (%s).
    print(story % (a_or_an, fruit))


class player:
    age = 5
    stamina = 5
    reflexes = 5
    brawn = 5
    wisdom = 5
    health = 100
    luck = 5
    name = ''

    def study(self):
        wisdom_gained = random.randrange(1, 10)
        self.wisdom += wisdom_gained
        print("You just gained " + str(wisdom_gained) + " wisdom!")

    def run(self):
        stamina_gained = random.randrange(1, 10)
        self.stamina += stamina_gained
        print("You just gained " + str(stamina_gained) + " stamina!")

    def attack(self, player):
        attack_value = random.randrange(0, 10)
        player.health -= attack_value
        print(self.name + " attacked " + player.name + " for " + str(attack_value) + " damage.")

    def __init__(self):
        self.name = input("What is your name?")
