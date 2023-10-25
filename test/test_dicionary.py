import unittest
from game.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary('dictionaries/diccionario.txt')

    def test_word_valid(self):
        self.assertTrue(self.dictionary.has_word('hola'))

    def test_word_not_valid(self):
        self.assertFalse(self.dictionary.has_word('awe'))
        
if __name__ == '__main__':
    unittest.main()



