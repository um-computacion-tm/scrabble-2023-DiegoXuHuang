import unittest
from game.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary('dictionaries/diccionario.txt')
      

    def test_word_valid(self):
        self.assertTrue(self.dictionary.has_word('hola'))

    def test_word_not_valid(self):
        self.assertFalse(self.dictionary.has_word('awe'))


    def test_remove_accents(self):
        word = 'café'
        self.assertEqual(self.dictionary.remove_accents(word), 'cafe')

    def test_remove_dieresis(self):
        word = 'pingüino'
        self.assertEqual(self.dictionary.remove_accents(word), 'pinguino')



    # def test_valid_word(self):
    #     # Prueba una palabra válida en minúsculas.
    #     word_validator = Dictionary(self.words)
    #     result = word_validator.is_valid_scrabble_word("hola")
    #     self.assertTrue(result)

    # def test_invalid_word(self):
    #     # Prueba una palabra no válida en minúsculas.
    #     word_validator = Dictionary(self.words)
    #     result = word_validator.is_valid_scrabble_word("www")
    #     self.assertFalse(result)

    # def test_word_with_mixed_case(self):
    #     # Prueba una palabra con mayúsculas y minúsculas.
    #     word_validator = Dictionary(self.words)
    #     result = word_validator.is_valid_scrabble_word("Mama")
    #     self.assertTrue(result)



        
if __name__ == '__main__':
    unittest.main()



