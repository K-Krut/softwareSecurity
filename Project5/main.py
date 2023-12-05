from typesofciphers import DataForEncryption, EncryptionType

if __name__ == '__main__':
    while True:
        data_for_processing = DataForEncryption(input('enter data:\n'))
        print(data_for_processing.process_data(EncryptionType(1)))
