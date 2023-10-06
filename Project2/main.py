from Project2.interface import CaesarCipherCLI
from Project2.logic import TritemiusCipher

if __name__ == "__main__":
    cipher = TritemiusCipher((2, 3))
    cli = CaesarCipherCLI(cipher)
    cli.run()
