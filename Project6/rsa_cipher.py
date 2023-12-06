from math import gcd, lcm
import os


class MerkleHellmanCipher:
    def __init__(self):
       pass
    # def encrypt(self, text):
    #     return " ".join([str(pow(ord(char), public_encryption_key[1]) % public_encryption_key[0]) for char in text])
    #
    # def decrypt(self, text):
    #     return "".join([chr(pow(int(one_number), private_encryption_key[1]) % private_encryption_key[0])
    #                     for one_number in text.split(" ")])

    @staticmethod
    def check_file(file):
        file_exist = not os.path.isfile(file) or os.path.getsize(file) == 0
        if not file_exist:
            user_answer = input("чи хочете ви змінити ключі? (yes or no)\n").strip().lower()
            return not file_exist and user_answer == "yes"
        return file_exist

    @staticmethod
    def validate_keys(keys):
        if not (len(keys) == 2 and all(map(str.isdigit, keys))):
            raise ValueError("Input must be two prime integers!")
        p, q = int(keys[0]), int(keys[1])

        for num in range(2, max(p, q)):
            if p > num and p % num == 0:
                raise ValueError("The 'p' number must be prime!")
            if q > num and q % num == 0:
                raise ValueError("The 'q' number must be prime!")
        return p, q

    @staticmethod
    def get_e(lcm_value):
        e = input(f"Type e. 1 < e < {lcm_value} & e co-prime to {lcm_value}").strip()
        if not e.isdigit():
            raise ValueError(f"e must be integer")
        e = int(e)
        if not lcm_value > e > 1 == gcd(e, lcm_value):
            raise ValueError(f"e must be 1 < e < {lcm_value} & e co-prime to {lcm_value}")
        return e

    @staticmethod
    def get_d(e, lcm_value):
        d = 1
        while (e * d) % lcm_value != 1:
            d += 1
        return d

    def rsa_encryption(self, arg_encrypt_or_decrypt, arg_chose_process):
        result_data = []
        file = "keys_data.txt"

        if self.check_file(file):
            p, q = self.validate_keys(input(f"type public and private keys").strip().split(" "))
            n = p * q
            lcm_value = lcm(p - 1, q - 1)

            e = self.get_e(lcm_value)
            d = self.get_d(e, lcm_value)

            public_key = [n, e]
            private_key = [n, d]

            with open(file, "wt") as file_for_save:
                file_for_save.write("\n".join(map(str, public_key + private_key)))
        else:
            with open(file, "rt") as file_for_save:
                key_info = file_for_save.read().split("\n")
            public_key = [int(key_info[0]), int(key_info[1])]
            private_key = [int(key_info[2]), int(key_info[3])]

        # encryption or decryption
        if arg_chose_process == "1":
            encrypted_data = [str(pow(ord(one_char), public_key[1]) % public_key[0])
                              for one_char in self.the_string_value]
            result_data.append(" ".join(encrypted_data))
        else:
            decrypted_data = [chr(pow(int(one_number), private_key[1]) % private_key[0])
                              for one_number in self.the_string_value.split(" ")]
            result_data.append("".join(decrypted_data))
        return result_data
