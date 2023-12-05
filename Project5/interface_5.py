class MerkleHellmanCipherCLI:
    def __init__(self, cipher):
        self.cipher = cipher
        self.text = ''
        self.dict_func = {
            '1': self.encrypt,
            '2': self.decrypt,
            '3': self.about,
            '4': self.exit_program,
        }

    def run(self):
        while True:
            print("1. Шифрувати текст\n"
                  "2. Розшифрувати текст\n"
                  "3. Про розробника\n"
                  "4. Вийти")
            try:
                self.dict_func[input("Введіть номер опції: ")]()
            except Exception as e:
                print(f"Введено невірну опцію: {e}")

    def encrypt(self):
        print(f'Зашифрований текст: {self.cipher.encrypt(input("Введіть текст для шифрування: "))}\n')

    def decrypt(self):
        print(f'Розшифрований текст: '
              f'{self.cipher.decrypt(input("Введіть текст: "))}\n')

    @staticmethod
    def about():
        print("Розробник: Kate Krut\nКонтакт: https://t.me/k_krut\n")

    @staticmethod
    def exit_program():
        print("Exiting")
        exit()
