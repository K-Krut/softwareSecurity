from Project1.exeptions import ValidateKeyIntError, ValidateKeyLengthError, ValidateTextError


class CaesarCipher:
    def __init__(self, alphabet, key):
        self.alphabet = alphabet
        self.key = key

    def check_key(self, key):
        if not isinstance(key, int):
            raise ValidateKeyIntError(key)
        if key < 0 or key >= len(self.alphabet):
            raise ValidateKeyLengthError()

    @staticmethod
    def check_text(text):
        for char in text:
            if char not in text:
                raise ValidateTextError(char)

    def get_index(self, char):
        return (self.alphabet.index(char) + self.key) % len(self.alphabet)

    def get_symbol(self, char, is_upper):
        index = self.get_index(char)
        return self.alphabet[index] if is_upper else self.alphabet[index].lower()

    def encrypt(self, text):
        self.check_key(self.key)  # self.check_text(text)
        encrypted_text = ""
        for char in text:
            is_upper = char.isupper()
            char = char.upper()
            encrypted_text += self.get_symbol(char, is_upper) if char in self.alphabet else char
        return encrypted_text

    def decrypt(self, text):
        self.check_key(self.key)
        decrypted_text = ""
        for char in text:
            is_upper = char.isupper()
            char = char.upper()
            if char in self.alphabet:
                index = (self.alphabet.index(char) - self.key) % len(self.alphabet)
                decrypted_text += self.alphabet[index] if is_upper else self.alphabet[index].lower()
            else:
                decrypted_text += char
        return decrypted_text

    def __str__(self):
        return f'alphabet: {self.alphabet}'
