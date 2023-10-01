import string

from Project1.exeptions import ValidateKeyIntError, ValidateKeyLengthError


class CaesarCipher:
    def __init__(self, key):
        self.english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ukrainian_alphabet = "АБВГҐДЕЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
        self.special_alphabet = string.digits + string.punctuation
        self.key = key

    def get_alphabet(self, char):
        for alphabet in [self.english_alphabet, self.ukrainian_alphabet, self.special_alphabet]:
            if char.upper() in alphabet:
                return alphabet
        return None

    def check_key(self, alphabet):
        if not isinstance(self.key, int):
            raise ValidateKeyIntError(self.key)
        if self.key < 0 or self.key >= len(alphabet):
            raise ValidateKeyLengthError()

    def get_index(self, char, alphabet):
        return (alphabet.index(char) + self.key) % len(alphabet)

    def get_index_decrypt(self, char, alphabet):
        return (alphabet.index(char) - self.key) % len(alphabet)

    def get_symbol(self, char, is_upper, alphabet, operation):
        self.check_key(alphabet)
        index = self.get_index(char, alphabet) if operation == 'encrypt' else self.get_index_decrypt(char, alphabet)
        return alphabet[index] if is_upper else alphabet[index].lower()

    def process_text(self, text, operation='encrypt'):
        result = ""
        for char in text:
            is_upper = char.isupper()
            char = char.upper()
            alphabet = self.get_alphabet(char)
            result += self.get_symbol(char, is_upper, alphabet, operation) if alphabet else char
        return result

    def encrypt(self, text):
        return self.process_text(text, operation='encrypt')

    def decrypt(self, text):
        return self.process_text(text, operation='decrypt')

    def __str__(self):
        return f'English Alphabet: {self.english_alphabet}\nUkrainian Alphabet: {self.ukrainian_alphabet}\n' \
               f'Special Alphabet: {self.special_alphabet}'
