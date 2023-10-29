from unidecode import unidecode

class Dictionary:
    def __init__(self, file_path):
        self.words = self.load_words(file_path)

    @staticmethod
    def load_words(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(word.strip() for word in file)

    def has_word(self, word):
        if isinstance(word, list):
            word = "".join(word).lower()
        else:
            word = word.lower()
        
        return word in self.words
    
    ''' CAMBIARLO A OTRA FORMA'''

    
    def remove_accents(self, word):
        word = word.lower()
        cleaned_word = unidecode(word)
        return cleaned_word

    def is_valid_scrabble_word(self, word):
        word = word.lower()  
        return word in self.words
    



