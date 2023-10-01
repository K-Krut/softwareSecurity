class CaesarCipherCLI:
    def __init__(self, cipher):
        self.cipher = cipher

    def run(self):
        while True:
            print("1. Відкрити файл")
            print("2. Зберегти файл")
            print("3. Шифрувати текст")
            print("4. Розшифрувати текст")
            print("5. Про розробника")
            print("6. Вийти")

            choice = input("Введіть номер опції: ")

            if choice == '1':
                self.open_file()
            elif choice == '2':
                self.save_file()
            elif choice == '3':
                self.encrypt()
            elif choice == '4':
                self.decrypt()
            elif choice == '5':
                self.about()
            elif choice == '6':
                break
            else:
                print("Невірний вибір, спробуйте знову.")

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
        print("Розробник: Ім'я Розробника\nКонтакт: example@example.com")
