"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:
    """Word Finder: finds random words from a text file."""
    def __init__(self, path):
        self.path = path
        self.words = self.read_file()
        print(f'{len(self.words)} words read')

    def read_file(self):
        'Opens and reads self.path and stores values in word_list list'
        file = open(self.path)

        word_list = []
        for line in file:
            line = line.rstrip('\n')
            word_list.append(line)
        # Replace with list comprehension

        return word_list

    def random(self):
        'Returns one random word from self.words list'
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    "Updated WordFinder that can read documents with '#' and spaces"

    def __init__(self, path):
        super().__init__(path)
    #  if no new parameter given, don't need a __init__

    # def random(self):
    #     """Selects one random word from WordFinder, and returns it if the word doesn't start
    #     with # or is an empty array. If conditions not met, the function will recursively call
    #     itself"""

    #     word = super().random()
    #     if len(word) != 0 and not word.startswith("#"):
    #         return word
    #     return self.random()

    def read_file(self):
        new_file = super().read_file()
        return [word for word in new_file if len(word) != 0 and not word.startswith("#")]
        
