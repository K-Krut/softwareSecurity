import string
import numpy as np
from Project2.logic import TritemiusCipher


class TritemiusAttack:
    def __init__(self):
        self.en_a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.uk_a = "АБВГҐДЕЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
        self.special_a = string.digits + string.punctuation

    def get_alphabet(self, char):
        for alphabet in [self.en_a, self.uk_a, self.special_a]:
            if char.upper() in alphabet:
                return alphabet
        return None

    @staticmethod
    def get_char_diff(char1, char2, alphabet):
        return (alphabet.index(char2) - alphabet.index(char1)) % len(alphabet)

    def get_differences(self, orig_text, encr_text):
        res = []
        for p, (char_orig, char_encr) in enumerate(zip(orig_text, encr_text)):
            alphabet = self.get_alphabet(char_orig)
            if alphabet:
                char_diff = self.get_char_diff(char_orig.upper(), char_encr.upper(), alphabet)
                res.append((p, char_diff, alphabet))
        return res[:2]


    @staticmethod
    def solve_2d(p1, p2, k1, k2, alphabet):
        """
        Вирішуємо матрицю рівнянь типу k = Ap + B;
        :param p1: номер 1 символу в тексті
        :param p2: номер 2 символу в тексті
        :param k1: різниця між оригінальним символом і зашифорованим для 1 символу тексту
        :param k2: різниця між оригінальним символом і зашифорованим для 2 символу тексту
        :param alphabet: алфавіт для символу
        :return: (key_value_1, key_value_2)
        """
        A = np.array([[p1, 1], [p2, 1]])
        B = np.array([k1, k2]) % len(alphabet)
        res = np.linalg.solve(A, B) % len(alphabet)
        return int(res[0]), int(res[1])

    def get_key(self, orig_text, encr_text):
        if len(orig_text) != len(encr_text):
            raise ValueError("Тексти не є парами")

        diff = self.get_differences(orig_text, encr_text)

        p1, k1, alphabet1 = diff[0]
        p2, k2, alphabet2 = diff[1]
        A, B = self.solve_2d(p1, p2, k1, k2, alphabet1)

        return A, B


cipher = TritemiusCipher((5, 7))
orig_text = "TАESTДрлНВ"
encr_text = cipher.encrypt(orig_text)
print(f"Оригінальний текст: {orig_text}\nЗашифрований текст: {encr_text}\n")
print(f"Ключ: {TritemiusAttack().get_key(orig_text, encr_text)}")
