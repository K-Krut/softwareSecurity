from Project1.logic import CaesarCipher
from Project2.logic import TritemiusCipher
from Project3.book_cipher import BookCipher


class CipherCLI:
    def __init__(self):
        self.ciphers = {
            '1': CaesarCipher(3),
            '2': TritemiusCipher((2, 4, 6)),
            '3': BookCipher()
        }
        self.current_cipher = None

    def run(self):
        while True:
            print("Виберіть шифр:\n"
                  "1. Шифр Цезаря\n"
                  "2. Шифр Тритеміуса\n"
                  "3. Книжковий шифр\n"
                  "4. Про розробника\n"
                  "5. Вийти")
            choice = input("Введіть номер опції: ")
            if choice == '4':
                self.about()
                return
            elif choice == '5':
                print("Exiting")
                exit()
            elif choice in self.ciphers:
                self.current_cipher = self.ciphers[choice]
                self.run_cipher_operations()
            else:
                print("Невірний вибір, спробуйте знову.")

    def run_cipher_operations(self):
        while True:
            print("Виберіть дію:\n"
                  "1. Шифрувати текст\n"
                  "2. Розшифрувати текст\n"
                  "3. Назад")
            choice = input("Введіть номер опції: ")
            if choice == '1':
                text = input("Введіть текст для шифрування: ")
                print(f'Зашифрований текст: {self.current_cipher.encrypt(text)}')
            elif choice == '2':
                text = input("Введіть текст для дешифрування: ")
                if isinstance(self.current_cipher, BookCipher):
                    sign = input("Введіть символ алфавіту тексту: ")
                    print(f'Розшифрований текст: {self.current_cipher.decrypt(text, sign)}')
                else:
                    print(f'Розшифрований текст: {self.current_cipher.decrypt(text)}')
            elif choice == '3':
                return
            else:
                print("Невірний вибір, спробуйте знову.")

    @staticmethod
    def about():
        print("Розробник: Kate Krut\nКонтакт: https://t.me/k_krut")

    @staticmethod
    def exit_program():
        print("Exiting")
        exit()
