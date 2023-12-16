from Crypto.PublicKey import RSA
from hashlib import sha1


class RSASignature:
    def __init__(self, file="result.txt"):
        self.file = file

    @staticmethod
    def get_hash(text):
        return int.from_bytes(sha1(bytes(text, "unicode-escape")).digest(), "big")

    @staticmethod
    def get_hash_signature(signature, e, n):
        return pow(signature, e, n)

    @staticmethod
    def get_keys():
        return RSA.generate(1024)

    @staticmethod
    def generate_signature(hash_data, keys):
        return pow(hash_data, keys.d, keys.n)

    def save_data_to_file(self, keys, signature):
        with open(self.file, "wt") as file:
            file.write(f"Public key:\nn = {keys.n}\ne = {keys.e}\n\n\nSignature: {signature}")

    def get_signature(self, text):
        hash_data = self.get_hash(text)
        keys = RSA.generate(1024)
        signature = self.generate_signature(hash_data, keys)
        self.save_data_to_file(keys, signature)
        return signature, keys.n, keys.e

    def check_signature(self, text, signature, n, e):
        return self.get_hash(text) == self.get_hash_signature(signature, e, n)

