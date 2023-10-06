from Project2.interface import TritemiusCipherCLI
from Project2.logic import TritemiusCipher

if __name__ == "__main__":
    cipher = TritemiusCipher((2, 3))
    cli = TritemiusCipherCLI(cipher)
    cli.run()
