import string


class TritemiusCipher:
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def encrypt(self, text, key):
        encrypted_text = ""
        for p, char in enumerate(text):
            if char in self.alphabet:
                x = self.alphabet.index(char)
                k = self.calculate_k(p, key)
                y = (x + k) % len(self.alphabet)
                encrypted_text += self.alphabet[y]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text, key):
        decrypted_text = ""
        for p, char in enumerate(text):
            if char in self.alphabet:
                y = self.alphabet.index(char)
                k = self.calculate_k(p, key)
                x = (y - k) % len(self.alphabet)
                decrypted_text += self.alphabet[x]
            else:
                decrypted_text += char
        return decrypted_text

    def calculate_k(self, p, key):
        if len(key) == 2:  # лінійне рівняння
            return key[0] * p + key[1]
        elif len(key) == 3:  # нелінійне рівняння
            return key[0] * p**2 + key[1] * p + key[2]
        else:  # гасло
            return self.alphabet.index(key[p % len(key)])

    def validate_key(self, key):
        if not (isinstance(key, tuple) or isinstance(key, str)):
            raise ValueError("Ключ повинен бути кортежем або рядком")
        if isinstance(key, tuple) and len(key) not in [2, 3]:
            raise ValueError("Довжина ключа для рівнянь повинна бути 2 або 3")

if __name__ == "__main__":
    alphabet = "АБВГҐДЕЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеежзиіїйклмнопрстуфхцчшщьюя"  # alphabet = "АБВГҐДЕЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеежзиіїйклмнопрстуфхцчшщьюя" + string.digits + string.punctuation + string.whitespace
    cipher = TritemiusCipher(alphabet)

    text = "БАНДЕРОЛЬ"
    linear_key = (2, 3)
    nonlinear_key = (1, 2, 3)
    passphrase_key = "ГАСЛО"

    encrypted_text = cipher.encrypt(text, linear_key)
    decrypted_text = cipher.decrypt(encrypted_text, linear_key)
    print(f"Original: {text}")
    print(f"Encrypted (linear): {encrypted_text}")
    print(f"Decrypted (linear): {decrypted_text}")

    encrypted_text = cipher.encrypt(text, nonlinear_key)
    decrypted_text = cipher.decrypt(encrypted_text, nonlinear_key)
    print(f"Encrypted (nonlinear): {encrypted_text}")
    print(f"Decrypted (nonlinear): {decrypted_text}")

    encrypted_text = cipher.encrypt(text, passphrase_key)
    decrypted_text = cipher.decrypt(encrypted_text, passphrase_key)
    print(f"Encrypted (passphrase): {encrypted_text}")
    print(f"Decrypted (passphrase): {decrypted_text}")
