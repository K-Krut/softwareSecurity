class CaesarCipherCLI:
    def __init__(self, cipher):
        self.cipher = cipher
        self.dict_func = {
            '1': self.open_file,
            '2': self.save_file,
            '3': self.encrypt,
            '4': self.decrypt,
            '5': self.about,
            '6': self.exit_program,
        }

    def run(self):

        while True:
            print("1. Відкрити файл\n"
                  "2. Зберегти файл\n"
                  "3. Шифрувати текст\n"
                  "4. Розшифрувати текст\n"
                  "5. Про розробника\n"
                  "6. Вийти")

            choice = input("Введіть номер опції: ")

            try:
                self.dict_func[choice]()
            except Exception as e:
                print(f"Введено невірну опцію: {e}")

    def open_file(self):
        file_path = input("Введіть шлях до файлу: ")
        try:
            with open(file_path, 'r') as file:
                self.text = file.read()
                print("Текст з файлу:")
                print(self.text)
        except Exception as e:
            print(f"Помилка при відкритті файлу: {e}")

    def save_file(self):
        file_path = input("Введіть шлях, де зберегти файл: ")
        try:
            with open(file_path, 'w') as file:
                file.write(self.text)
                print("Файл успішно збережено.")
        except Exception as e:
            print(f"Помилка при збереженні файлу: {e}")

    def encrypt(self):
        text = input("Введіть текст для шифрування: ")
        print(text)
        print(self.cipher)
        print("Зашифрований текст:")
        print(self.cipher.encrypt(text))

    def decrypt(self):
        text = input("Введіть текст для розшифрування: ")
        print("Розшифрований текст:")
        print(self.cipher.decrypt(text))

    def about(self):
        print("Розробник: Kate Krut\nКонтакт: https://t.me/k_krut")

    def exit_program(self):
        print("Exiting")
        exit()
