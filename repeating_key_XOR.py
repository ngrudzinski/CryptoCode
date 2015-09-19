import binascii

FIXED_PLAINTEXT = 'Burning \'em, if you ain\'t quick and nimble I go crazy when I hear a cymbal'
FIXED_KEY = 'ICE'


def repeating_key(plaintext, key):
    plaintext_bin = bin(int(binascii.hexlify(plaintext), 16))[2:].zfill(len(plaintext)*8)
    key_bin_original = bin(int(binascii.hexlify(key), 16))[2:].zfill(len(key)*8)
    key_bin_len = len(key_bin_original)
    plaintext_bin_len = len(plaintext_bin)
    remainder = plaintext_bin_len % key_bin_len
    key_bin = ''
    for i in range(0, plaintext_bin_len // key_bin_len):
        key_bin += key_bin_original
    if remainder != 0:
        key_bin += key_bin_original[0:remainder]
    result_bin = ''
    for k in range(0, plaintext_bin_len):
        xor_char = int(plaintext_bin[k]) ^ int(key_bin[k])
        result_bin += str(xor_char)
    result_hex = hex(int(result_bin, 2))[2:].rstrip('L')
    return result_hex

if __name__ == '__main__':
    print(repeating_key(FIXED_PLAINTEXT, FIXED_KEY))