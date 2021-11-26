import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_empty_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KUNSDLGEW')
        self.assertEqual(new_game.is_valid(''), False)
        self.assertEqual(new_game.grid, list('KUNSDLGEW'))
        
    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list('KUNSDLGEW')
        self.assertEqual(new_game.is_valid('DUNE'), True)
        self.assertEqual(new_game.grid, list('KUNSDLGEW'))

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KUNSDLGEW')
        self.assertEqual(new_game.is_valid('DUNCE'), False)
        self.assertEqual(new_game.grid, list('KUNSDLGEW'))

    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
      self.assertIs(new_game.is_valid('FEUN'), False)