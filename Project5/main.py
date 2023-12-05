from Project5.interface_5 import MerkleHellmanCipherCLI
from merkle_hellman_cipher import MerkleHellmanCipher

if __name__ == '__main__':
    # MerkleHellmanCipherCLI(MerkleHellmanCipher('2 7 11 21 42 89 180 354', '881 588')).run()
    sequence = input("Введіть послідовність: ").strip().split(" ")
    keys = input("Введіть q і r. q > суми послідовності & r взаємно просте до q: ").strip().split(" ")
    MerkleHellmanCipherCLI(MerkleHellmanCipher(sequence, keys)).run()
