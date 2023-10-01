from Project1.interface import CaesarCipherCLI
from Project1.logic import CaesarCipher

if __name__ == "__main__":
    cipher = CaesarCipher(12)
    cli = CaesarCipherCLI(cipher)
    cli.run()
