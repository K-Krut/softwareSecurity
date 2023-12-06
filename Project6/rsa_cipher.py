from math import gcd, lcm
import os


class RSACipher:
    def __init__(self, keys=(None, None), file="keys\\keys_data.txt"):
    # def __init__(self, keys=(None, None), file="saved_key_info\\lab6_saved_key_info.txt"):
    # def __init__(self, file="keys_data.txt"):
        self.file = file
        self.public_key, self.private_key = keys  # self.get_public_private_keys(keys)

    def check_file_exist(self):
        return not os.path.isfile(self.file) or os.path.getsize(self.file) == 0

    @staticmethod
    def validate_keys(keys):
        if not (len(keys) == 2 and all(map(str.isdigit, keys))):
            raise ValueError("числа мають бути простими і цілими")
        p, q = int(keys[0]), int(keys[1])

        for num in range(2, max(p, q)):
            if p > num and p % num == 0:
                raise ValueError("p має бути простим")
            if q > num and q % num == 0:
                raise ValueError("q має бути простим")
        return p, q

    @staticmethod
    def get_e(lcm_value):
        e = input(f"1 < e < {lcm_value} & e взаємно просте до {lcm_value}: ").strip()
        if not e.isdigit():
            raise ValueError(f"e має бути цілим")
        e = int(e)
        if not lcm_value > e > 1 == gcd(e, lcm_value):
            raise ValueError(f"1 < e < {lcm_value} & e взаємно просте до {lcm_value}")
        return e

    @staticmethod
    def get_d(e, lcm_value):
        d = 1
        while (e * d) % lcm_value != 1:
            d += 1
        return d

    def get_public_private_keys(self, keys=None):
        p, q = self.validate_keys(keys)
        n = p * q
        lcm_value = lcm(p - 1, q - 1)

        e = self.get_e(lcm_value)
        d = self.get_d(e, lcm_value)

        public_key = [n, e]
        private_key = [n, d]

        with open(self.file, "wt") as file:
            file.write("\n".join(map(str, public_key + private_key)))

        self.public_key, self.private_key = public_key, private_key
        return public_key, private_key

    def read_public_private_keys(self):
        with open(self.file, "rt") as file:
            data = file.read().split("\n")
        public_key = [int(data[0]), int(data[1])]
        private_key = [int(data[2]), int(data[3])]

        self.public_key, self.private_key = public_key, private_key
        return public_key, private_key


    def encrypt(self, text):
        return " ".join([str(pow(ord(char), self.public_key[1]) % self.public_key[0]) for char in text])

    def decrypt(self, text):
        return "".join([chr(pow(int(num), self.private_key[1]) % self.private_key[0]) for num in text.split(" ")])


# rsa = RSACipher()
# rsa.read_public_private_keys()
# print(rsa.encrypt('test'))
# print(rsa.decrypt('51 82 19 51'))


# rsa = RSACipher()
# rsa.get_public_private_keys('61 53'.strip().split(" "))
# print(rsa.decrypt(rsa.encrypt('test')))


# rsa = RSACipher()
# rsa.read_public_private_keys()
# print(rsa.decrypt(rsa.encrypt('test')))
