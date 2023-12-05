import random
import re
import string
from poems import *


class BookCipher:
    def __init__(self):
        self.en_alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.uk_alphabet = "абвгґдежзиіїйклмнопрстуфхцчшщьюя"
        self.special_alphabet = string.digits + string.punctuation
        self.poems = {
            self.en_alphabet: self.generatePoem(POEM_EN),
            self.uk_alphabet: self.generatePoem(POEM_UK)
        }
        self.key = 1

    @staticmethod
    def generatePoem(poem):
        poem_dict = {}
        for numerator, line in enumerate(poem.split('\n'), start=1):
            for denominator, char in enumerate(line, start=1):
                poem_dict[f'{numerator}/{denominator}'] = char
        return poem_dict

    def validate_text(self, text_letters):
        if not text_letters:
            raise ValueError('Некоректний текст. Текст має містити літери')
        if not self.check_text_belogs_to_one_alphabet(text_letters):
            raise ValueError('Всі літери тексту мають належати одному алфавіту (до однієї сови)')

    @staticmethod
    def check_key_format(key, alphabet):
        try:
            numerator, denominator = map(int, key.split('/'))
            return not (denominator == 0 or (numerator == 0 and not 1 <= denominator <= len(alphabet)))
        except (ValueError, IndexError):
            return False

    def validate_text_decrypt(self, text, alphabet, poem):
        for key in text.split(', '):
            if key not in self.special_alphabet:
                if not self.check_key_format(key, alphabet):
                    raise ValueError(f'Помилка в шифрі, некоректний ключ {key}')

    @staticmethod
    def check_key_is_in_poem(key, poem_keys):
        return key in poem_keys

    def validate_char_for_decrypt(self, alphabet_char):
        if not isinstance(alphabet_char, str):
            raise ValueError('Введено не символ. Приклад символу "a"')
        if not alphabet_char.isalpha():
            raise ValueError('Символ для визначення мови віршу некоректний')
        alphabet = self.get_alphabet_by_char(alphabet_char)
        if not alphabet:
            raise ValueError('Символ не належить жодній доступній мові віршу ')
        return alphabet

    def get_poem(self, char):
        for alphabet in [self.en_alphabet, self.uk_alphabet]:
            if char in alphabet:
                return self.poems[alphabet]
        return None

    def get_alphabet_by_char(self, char):
        for alphabet in [self.en_alphabet, self.uk_alphabet]:
            if char in alphabet:
                return alphabet
        return None

    def get_non_poem_char(self, char):
        alphabet = self.get_alphabet_by_char(char)
        return f'0/{alphabet.index(char)}' if alphabet else char

    def check_text_belogs_to_one_alphabet(self, text):
        return any(set(text) <= set(alphabet) for alphabet in [self.en_alphabet, self.uk_alphabet])

    def get_symbol(self, char, poem):
        keys = [key for key, value in poem.items() if value == char]
        return random.choice(keys) if len(keys) > 0 else self.get_non_poem_char(char)

    def get_symbol_decrypt(self, key, poem, poem_keys, alphabet):
        return poem[key] if self.check_key_is_in_poem(key, poem_keys) else alphabet[int(key.split('/')[1])] if \
            key.split('/')[0] == '0' else '(?)' if self.check_key_format(key, alphabet) else key

    def encrypt(self, text):
        text = text.lower().strip()
        text_letters = re.sub(r'[^a-zA-ZА-Яа-я]', '', text)
        self.validate_text(text_letters)
        poem = self.get_poem(text_letters[0])
        return ", ".join([self.get_symbol(char, poem) for char in text])

    def decrypt(self, text, alphabet_char):
        alphabet = self.validate_char_for_decrypt(alphabet_char)
        poem = self.poems[alphabet]
        poem_keys = [poem_key for poem_key in poem.keys()]
        self.validate_text_decrypt(text.strip(), alphabet, poem)
        return ''.join([self.get_symbol_decrypt(char, poem, poem_keys, alphabet) for char in text.strip().split(', ')])

    def __str__(self):
        return 'BookCipher'

