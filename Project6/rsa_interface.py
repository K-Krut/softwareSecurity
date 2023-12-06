from Project6.rsa_cipher import RSACipher


class RSACipherCLI:
    def __init__(self, cipher=RSACipher()):
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

    def check_file(self):
        file_exist = self.cipher.check_file_exist()
        if not file_exist:
            user_answer = input("чи хочете ви змінити ключі? (yes or no)\n").strip().lower()
            return not file_exist and user_answer == "yes"
        return file_exist
    
    def encrypt(self):
        if self.check_file():
            self.cipher.get_public_private_keys(input(f"Введіть public & private ключі: ").strip().split(" "))
        self.cipher.read_public_private_keys()
        print(f'Зашифрований текст: {self.cipher.encrypt(input("Введіть текст для шифрування: "))}\n')

    def decrypt(self):
        if self.check_file():
            self.cipher.get_public_private_keys(input(f"Введіть public & private ключі: ").strip().split(" "))
        self.cipher.read_public_private_keys()
        print(f'Розшифрований текст: {self.cipher.decrypt(input("Введіть текст: "))}\n')

    @staticmethod
    def about():
        print("Розробник: Kate Krut\nКонтакт: https://t.me/k_krut\n")

    @staticmethod
    def exit_program():
        print("Exiting")
        exit()
