from Project5.interface_5 import MerkleHellmanCipherCLI
from merkle_hellman_cipher import MerkleHellmanCipher, EncryptionType

if __name__ == '__main__':
    MerkleHellmanCipherCLI(MerkleHellmanCipher('2 7 11 21 42 89 180 354', '881 588')).run()
#     while True:
#         data_for_processing = MerkleHellmanCipher(input('enter data:\n'))
#         print(data_for_processing.process_data(EncryptionType(1)))


