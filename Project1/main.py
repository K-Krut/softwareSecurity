from Project1.interface import CaesarCipherCLI
from Project1.logic import CaesarCipher

if __name__ == "__main__":
    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ukrainian_alphabet = "АБВГҐДЕЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
    key = 4
    cipher = CaesarCipher(english_alphabet, ukrainian_alphabet, key)
    cli = CaesarCipherCLI(cipher)
    cli.run()
