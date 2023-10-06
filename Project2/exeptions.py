class ValidateKeyError(Exception):
    def __init__(self, key, error_message='Ключ повинен бути кортежем або рядком'):
        self._key = key
        self._error_message = error_message
        super().__init__(self._error_message)

    def __str__(self):
        return f'{self._error_message}:\nKey / Value:{self._key}'


class ValidateKeyLengthError(Exception):
    def __init__(self, error_message="Довжина ключа для рівнянь повинна бути 2 або 3"):
        self._error_message = error_message
        super().__init__(self._error_message)

    def __str__(self):
        return f'{self._error_message}'
