from Project2.interface import TritemiusCipherCLI
from Project2.logic import TritemiusCipher

if __name__ == "__main__":
    cipher = TritemiusCipher('keyfortest')
    # cipher = TritemiusCipher((2, 3))
    # cipher = TritemiusCipher((2, 4, 6))
    TritemiusCipherCLI(cipher).run()
