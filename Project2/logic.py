import string
from Project2.exeptions import ValidateKeyError, ValidateKeyLengthError


class TritemiusCipher:
    def __init__(self, key):
        self.en_a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.uk_a = "АБВГҐДЕЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
        self.special_a = string.digits + string.punctuation
        self.validate_key(key)
        self.key = key
        self.key_alphabet = None
        if isinstance(key, str):
            self.key_alphabet = self.identify_key_alphabet(key)

    def get_alphabet(self, char):
        for alphabet in [self.en_a, self.uk_a, self.special_a]:
            if char.upper() in alphabet:
                return alphabet
        return None

    def key_value_check(self, value):
        return value < 0 or any(value >= x for x in
                                [len(self.uk_a), len(self.en_a),
                                 len(self.special_a)])

    def check_str_key(self, key):
        return all(char.upper() in self.uk_a or char in self.en_a or char in self.special_a for char in key)

    def identify_key_alphabet(self, key):
        return self.uk_a if key[0].upper() in self.uk_a else \
            self.en_a if key[0].upper() in self.en_a else self.special_a

    def validate_key(self, key):
        if not (isinstance(key, tuple) or isinstance(key, str)):
            raise ValidateKeyError(key)
        if isinstance(key, tuple) and len(key) not in [2, 3]:
            raise ValidateKeyLengthError()
        if isinstance(key, tuple):
            for value in key:
                if not isinstance(value, int):
                    raise ValidateKeyError(value, "Значення не є цілим числом")
                if self.key_value_check(value):
                    raise ValidateKeyError(value, 'Одне із значень ключа більше ніж може бути')
        if isinstance(key, str):
            if self.key_value_check(len(key)):
                raise ValidateKeyError(key, f'Довжина ключа ({len(key)}) більшa ніж може бути')
            if not self.check_str_key(key):
                ValidateKeyError(key, f'Всі символи ключа мабть належати до одного алфавіту')
            # self.key_alphabet = self.identify_key_alphabet(key)

    def get_k(self, p):
        if isinstance(self.key, tuple):
            if len(self.key) == 2:
                return self.key[0] * p + self.key[1]
            if len(self.key) == 3:
                return self.key[0] * p ** 2 + self.key[1] * p + self.key[2]
        return self.key_alphabet.index(self.key[p % len(self.key)].upper())

    def get_index(self, char, alphabet, p):
        return (alphabet.index(char) + self.get_k(p)) % len(alphabet)

    def get_index_decrypt(self, char, alphabet, p):
        return (alphabet.index(char) + len(alphabet) - (self.get_k(p) % len(alphabet))) % len(alphabet)

    def get_symbol(self, char, is_upper, alphabet, p, operation):
        index = self.get_index(char, alphabet, p) if operation == 'encrypt' else self.get_index_decrypt(char, alphabet, p)
        return alphabet[index] if is_upper else alphabet[index].lower()

    def process_text(self, text, operation='encrypt'):
        result = ""
        for char in text:
            p = text.index(char)
            is_upper = char.isupper()
            char = char.upper()
            alphabet = self.get_alphabet(char)
            result += self.get_symbol(char, is_upper, alphabet, p, operation) if alphabet else char
        return result

    def encrypt(self, text):
        return self.process_text(text, operation='encrypt')

    def decrypt(self, text):
        return self.process_text(text, operation='decrypt')

    def __str__(self):
        return f'English Alphabet: {self.en_a}\nUkrainian Alphabet: {self.uk_a}\n' \
               f'Special Alphabet: {self.special_a}'
