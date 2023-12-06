from TypesOfCiphers import DataForEncryption, EncryptionType

if __name__ == '__main__':
    print("Hello! This program for encrypting and decrypting text, choose encryption type below:")

    all_encryption_types = []
    all_encryption_types_values = []
    for one_encryption_type in EncryptionType:
        one_encryption_name = one_encryption_type.name
        if "Cipher" in one_encryption_name:
            one_encryption_name = one_encryption_name.replace("Cipher", "")
        all_encryption_types.append(f"{one_encryption_type.value}. {one_encryption_name} cipher")
        all_encryption_types_values.append(str(one_encryption_type.value))
    while True:
        for the_encryption_type_string in all_encryption_types:
            print(the_encryption_type_string)
        while True:

            chose_cipher = input().strip()
            if chose_cipher in all_encryption_types_values:
                break
            else:
                print(f"Wrong input! Type number {', '.join(all_encryption_types_values[:-1])} or "
                      f"{all_encryption_types_values[-1]} and nothing else")
        print("Choose one options among all below:")
        chosen_encryption_type = EncryptionType(int(chose_cipher))

        print("1. Read from file")
        print("2. Read from console")
        print("3. Quit")
        user_answer = input().strip()
        if user_answer == "1":
            while True:
                print("Print name of file (whole path)")
                printed_name_of_file = input()
                try:
                    chosen_file = open(printed_name_of_file)
                    file_content = chosen_file.read()
                    print("Data from file:")
                    print(file_content)
                    data_for_processing = DataForEncryption(file_content)
                    print(data_for_processing.process_data(chosen_encryption_type))
                    break
                except FileNotFoundError:
                    print("File doesn't exist! Type Enter and try again or type now letter 'q' (or 'Q') and quit")
                    temp_answer = input()
                    if temp_answer.lower() == 'q':
                        break
        elif user_answer == "2":
            print("Print some string in the console")
            printed_data = input()
            data_for_processing = DataForEncryption(printed_data)
            print(data_for_processing.process_data(chosen_encryption_type))
        elif user_answer == "3":
            break
        else:
            print("Wrong input! Type number 1, 2 or 3 and nothing else")
        print("Hello again! This program for encrypting and decrypting text, choose encryption type below:")
