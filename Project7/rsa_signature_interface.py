from Project7.rsa_signature import RSASignature


class RSASignatureCLI:
    def __init__(self, cipher=RSASignature()):
        self.cipher = cipher
        self.text = ''
        self.dict_func = {
            '1': self.get_signature,
            '2': self.check_signature,
            '3': self.about,
            '4': self.exit_program,
        }

    def run(self):
        while True:
            print("1. Отримати Підпис\n"
                  "2. Перевірити підпис\n"
                  "3. Про розробника\n"
                  "4. Вийти")
            try:
                self.dict_func[input("Введіть номер опції: ")]()
            except Exception as e:
                print(f"Введено невірну опцію: {e}")

    def get_signature(self):
        result = self.cipher.get_signature(input("Введіть текст для шифрування: "))
        print(f"Підпис: {result[0]}\n Public Key n = {result[1]}\n Public Key e = {result[2]}\n\n"
              f"Інформацію додатково збережено в файл\n\n\n")

    def check_signature(self):
        text = input("Введіть текст: ")
        signature = int(input("Введіть підпис: "))
        n = int(input("Введіть key n: "))
        e = int(input("Введіть key e: "))
        print(f'Результат: {self.cipher.check_signature(text, signature, n, e)}\n')

    @staticmethod
    def about():
        print("Розробник: Kate Krut\nКонтакт: https://t.me/k_krut\n")

    @staticmethod
    def exit_program():
        print("Exiting")
        exit()
