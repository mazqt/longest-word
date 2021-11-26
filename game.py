import random
import string
import requests

class Game:
    def __init__(self):
        self.grid = random.sample(string.ascii_uppercase, 9)

    def is_valid(self, word):
        if word == "":
             return False
        else:
            letters = self.grid[:]
            for letter in list(word):
                if letter in letters:
                    letters.remove(letter)
                else:
                    return False
        return self.__check_dictionary(word)


    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']