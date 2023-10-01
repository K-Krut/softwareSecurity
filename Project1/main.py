from Project1.interface import CaesarCipherCLI
from Project1.logic import CaesarCipher

if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГҐДЕЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
    key = 1
    cipher = CaesarCipher(alphabet, key)
    cli = CaesarCipherCLI(cipher)
    cli.run()
