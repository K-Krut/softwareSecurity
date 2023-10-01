class ValidateKeyIntError(Exception):
    def __init__(self, key, error_message='Ключ повинен бути цілим числом'):
        self._key = key
        self._error_message = error_message
        super().__init__(self._error_message)

    def __str__(self):
        return f'{self._error_message}:\n{self._key} не є цілим числом'


class ValidateKeyLengthError(Exception):
    def __init__(self, error_message='Ключ повинен бути в межах довжини алфавіту'):
        self._error_message = error_message
        super().__init__(self._error_message)

    def __str__(self):
        return f'{self._error_message}'


class ValidateTextError(Exception):
    def __init__(self, char, error_message='Некоректний символ'):
        self._char = char
        self._error_message = error_message
        super().__init__(self._error_message)

    def __str__(self):
        return f'{self._error_message}. Символ {self._char} не може бути зашифрований'
