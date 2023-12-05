from enum import Enum
from math import gcd


class EncryptionType(Enum):
    MerkleHellman = 1


class MerkleHellmanCipher:
    def __init__(self, sequence=None, keys=None):
        self.sequence = self.validate_sequence(sequence)
        self.keys = self.validate_keys(keys, sequence)

    # def process_data(self, arg_encryption_type: EncryptionType):
    #     chose_process = ""
    #     while True:
    #         print("Choose one options among all below")
    #         print("1. Encrypt data")
    #         print("2. Decrypt data")
    #         chose_process = input().strip()
    #         if chose_process in ("1", "2"):
    #             break
    #         else:
    #             print("Wrong input! Type number 1 or 2 and nothing else")
    #
    #     result_data = []
    #
    #     if arg_encryption_type == EncryptionType.MerkleHellman:
    #         result_data = self.merkle_hellman_encryption(chose_process)
    #     return "Result:\n" + "".join(result_data) + "\n"

    @staticmethod
    def check_sequence_increasing(sequence):
        return all([sequence[num] > sum(sequence[:num]) for num in range(1, len(sequence))])

    @staticmethod
    def check_sequence_digits(input_):
        return all(map(str.isdigit, input_))

    def get_sequence(self):
        while True:
            input_sequence = input("type super-increasing sequence of positive integers").strip().split(" ")

            if self.check_sequence_digits(input_sequence):
                sequence = list(map(int, input_sequence))
                if self.check_sequence_increasing(sequence):
                    return sequence
                print("Sequence of positive integers must be super-increasing!")
            print("sequence must be super-increasing of positive integers!")

    def validate_sequence(self, input_sequence):
        input_sequence = input_sequence.strip().split(" ")
        if not self.check_sequence_digits(input_sequence):
            raise ValueError('Послідовність має складатись лише з цифр')
        sequence = list(map(int, input_sequence))
        if not self.check_sequence_increasing(sequence):
            raise ValueError('Послідовність має бути супер-зростаючою')
        return sequence

    def get_keys(self, sequence):
        while True:
            print("type 'q' and 'r' such that 'q' > sum of super increasing sequence & 'r' co-prime to 'q'")
            q_r_values = input().strip().split(" ")

            if self.check_sequence_digits(q_r_values):
                q_value, r_value = int(q_r_values[0]), int(q_r_values[1])
                if q_value <= sum(sequence):
                    print("The 'q' value must be greater than the sum of super increasing sequence !")
                elif gcd(q_value, r_value) != 1:
                    print("The 'r' number must be co-prime to 'q'! (GCD(q, r) = 1)")
                return q_value, r_value
            print("Input must be two integers!")

    def validate_keys(self, q_r_values, sequence):
        q_r_values = q_r_values.strip().split(" ")
        if not self.check_sequence_digits(q_r_values):
            raise ValueError('Input must be two integers!')
        q, r = int(q_r_values[0]), int(q_r_values[1])
        if not q <= sum(sequence):
            raise ValueError("The 'q' value must be greater than the sum of super increasing sequence !")
        if not gcd(q, r) != 1:
            raise ValueError("The 'r' number must be co-prime to 'q'! (GCD(q, r) = 1)")
        return q, r

    @staticmethod
    def get_bit(char):
        return bin(ord(char))[2:]

    def get_bit_result(self, seq_len, char):
        bit = self.get_bit(char)
        bit_len = len(bit)
        return "0" * (seq_len - bit_len) + bit if bit_len < seq_len else \
            (bit[:seq_len + 1] if bit_len > seq_len else bit)

    @staticmethod
    def get_encrypted_char(bit, key):
        return sum(int(bit[bit_index]) * key[bit_index] for bit_index in range(len(bit)))

    def encrypt(self, text, sequence_len, key):
        bit_result = [self.get_bit_result(sequence_len, char) for char in text]
        return " ".join([str(self.get_encrypted_char(bit, key)) for bit in bit_result])

    @staticmethod
    def get_number_inverse(num, r_inverse, q_value):
        return (int(num) * r_inverse) % q_value

    def get_decrypted_char(self, number, sequence, sequence_len, r_inverse, q_value):
        dec_char_num = 0
        num_inverse = self.get_number_inverse(number, r_inverse, q_value)
        for index in range(len(sequence) - 1, -1, -1):
            if sequence[index] <= num_inverse:
                num_inverse -= sequence[index]
                dec_char_num += pow(2, sequence_len - index - 1)
        return dec_char_num

    @staticmethod
    def get_r_inverse(r_value, q_value):
        r_inverse = 1
        while (r_value * r_inverse) % q_value != 1:
            r_inverse += 1
        return r_inverse

    def decrypt(self, text, r, q, sequence):
        enc_values = text.split(" ")
        r_inverse = self.get_r_inverse(r, q)
        return "".join([chr(self.get_decrypted_char(num, sequence, len(sequence), r_inverse, q)) for num in enc_values])

    def merkle_hellman_encryption(self, text, choose):
        sequence = self.get_sequence()
        q, r = self.get_keys(sequence)
        key = [(private_value * r) % q for private_value in sequence]
        return self.encrypt(text, len(sequence), key) if choose == "1" else self.decrypt(text, r, q, sequence)


# if __name__ == '__main__':
#     print(DataForEncryption('aHelloWorld!').
#           merkle_hellman_encryption("1"))

