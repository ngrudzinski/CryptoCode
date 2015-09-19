FIXED_HEX = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'


def detect_words(bin_string):
    cnt = 0
    for i in range(0, len(bin_string), 8):
        dec = int(bin_string[i:i+8], 2)
        if dec in range(32, 127):
            cnt += 1
    if cnt == len(bin_string)/8:
        return 1
    return 0


def xor_2_strings(encoded_hex):
    scale = 16
    length = len(encoded_hex)
    num_of_bits = length * 4

    binary_string = bin(int(encoded_hex, scale))[2:].zfill(num_of_bits)
    binary_array = list(binary_string)

    for i in range(0, 256):
        # this next line creates byte sized strings of 0 to 256 in binary
        bin_i8 = bin(i)[2:].zfill(8)
        bin_i = bin_i8 * (length/2)
        bin_i_array = list(bin_i)
        xor_string = ''
        for k in range(0, (length*4)):
            xor_char = int(binary_array[k]) ^ int(bin_i_array[k])
            xor_string += str(xor_char)
        # at this point xor_string is the correct xor of the byte and string
        if detect_words(xor_string) == 1:
            print(chr(i) + "    " + ''.join(chr(int(xor_string[i:i+8], 2)) for i in range(0, len(xor_string), 8)))

if __name__ == "__main__":
    xor_2_strings(FIXED_HEX)