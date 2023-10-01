class CaesarCipher:
    def __init__(self, alphabet, key):
        self.alphabet = alphabet
        self.key = key

    def check_key(self, key):
        if not isinstance(key, int):
            raise ValueError("Ключ повинен бути цілим числом")
        if key < 0 or key >= len(self.alphabet):
            raise ValueError("Ключ повинен бути в межах довжини алфавіту")

    def check_text(self, text):
        for char in text:
            if char not in text:
                raise ValueError("Ключ повинен бути цілим числом")

    def encrypt(self, text):
        self.check_key(self.key)
        encrypted_text = ""
        for char in text:
            is_upper = char.isupper()
            char = char.upper()
            if char in self.alphabet:
                index = (self.alphabet.index(char) + self.key) % len(self.alphabet)
                if not is_upper:
                    encrypted_text += self.alphabet[index].lower()
                else:
                    encrypted_text += self.alphabet[index]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text):
        self.check_key(self.key)
        decrypted_text = ""
        for char in text:
            is_upper = char.isupper()
            char = char.upper()
            if char in self.alphabet:
                index = (self.alphabet.index(char) - self.key) % len(self.alphabet)
                if not is_upper:
                    decrypted_text += self.alphabet[index].lower()
                else:
                    decrypted_text += self.alphabet[index]
            else:
                decrypted_text += char
        return decrypted_text

    def __str__(self):
        return f'alphabet: {self.alphabet}, key: {self.key}'
