from Project1.exeptions import ValidateKeyIntError, ValidateKeyLengthError, ValidateTextError


class CaesarCipher:
    def __init__(self, english_alphabet, ukrainian_alphabet, key):
        self.english_alphabet = english_alphabet
        self.ukrainian_alphabet = ukrainian_alphabet
        self.key = key

    def get_alphabet(self, char):
        if char.upper() in self.english_alphabet:
            return self.english_alphabet
        elif char.upper() in self.ukrainian_alphabet:
            return self.ukrainian_alphabet
        else:
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
        return f'English Alphabet: {self.english_alphabet}\nUkrainian Alphabet: {self.ukrainian_alphabet}'
