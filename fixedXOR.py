ORIGINAL = '1c0111001f010100061a024b53535009181c'
XOR = '686974207468652062756c6c277320657965'


def xor_2_strings(original_string, xor_string):
    scale = 16
    length = len(original_string)
    num_of_bits = length * 4

    original_binary = bin(int(original_string, scale))[2:].zfill(num_of_bits)
    xor_binary = bin(int(xor_string, scale))[2:].zfill(num_of_bits)

    result_binary = ''
    for i in range(0, num_of_bits):
        result_char = int(original_binary[i]) ^ int(xor_binary[i])
        result_binary += str(result_char)
    hex_string = hex(int(result_binary, 2))[2:].rstrip('L')
    print(hex_string)

if __name__ == "__main__":
    xor_2_strings(ORIGINAL, XOR)