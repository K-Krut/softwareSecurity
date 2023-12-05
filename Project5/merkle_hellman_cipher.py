from math import gcd


class MerkleHellmanCipher:
    def __init__(self, sequence=None, keys=None):
        self.sequence = self.validate_sequence(sequence)
        self.q, self.r = self.validate_keys(keys, self.sequence)
        self.key = self.get_key(self.r, self.q, self.sequence)

    @staticmethod
    def get_key(r, q, sequence):
        return [(private_value * r) % q for private_value in sequence]

    @staticmethod
    def check_sequence_increasing(sequence):
        return all([sequence[num] > sum(sequence[:num]) for num in range(1, len(sequence))])

    @staticmethod
    def check_sequence_digits(input_):
        return all(map(str.isdigit, input_))

    def validate_sequence(self, input_sequence):
        if not self.check_sequence_digits(input_sequence):
            raise ValueError('Послідовність має складатись лише з цифр')
        sequence = list(map(int, input_sequence))
        if not self.check_sequence_increasing(sequence):
            raise ValueError('Послідовність має бути суперзростаючою')
        return sequence

    def validate_keys(self, q_r_values, sequence):
        if not self.check_sequence_digits(q_r_values):
            raise ValueError('Input must be two integers!')
        q, r = int(q_r_values[0]), int(q_r_values[1])
        if q <= sum(sequence):
            raise ValueError("q має бути більшим суми послідовності!")
        if gcd(q, r) != 1:
            raise ValueError("r має бути взаємно простим до q! GCD(q, r) = 1")
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

    def encrypt(self, text):
        bit_result = [self.get_bit_result(len(self.sequence), char) for char in text]
        return " ".join([str(self.get_encrypted_char(bit, self.key)) for bit in bit_result])

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

    def decrypt(self, text):
        enc_values = text.split(" ")
        r_inverse = self.get_r_inverse(self.r, self.q)
        return "".join([chr(self.get_decrypted_char(num, self.sequence, len(self.sequence), r_inverse, self.q))
                        for num in enc_values])
