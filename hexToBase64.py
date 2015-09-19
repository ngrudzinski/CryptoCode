hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'


def hex2binary(string):
    return bin(int(string, 16))[2:].zfill(4)


def binary2base64(binary):
    length = len(binary)
    mod = length % 6 - 4
    binary = ('0' * mod) + binary
    # make binary into an array of 6 digits elements
    binary = [binary[i:i+6] for i in range(0, len(binary), 6)]
    for n, element in enumerate(binary):
        if element == '000000':
            binary[n] = 'A'
        elif element == '000001':
            binary[n] = 'B'
        elif element == '000010':
            binary[n] = 'C'
        elif element == '000011':
            binary[n] = 'D'
        elif element == '000100':
            binary[n] = 'E'
        elif element == '000101':
            binary[n] = 'F'
        elif element == '000110':
            binary[n] = 'G'
        elif element == '000111':
            binary[n] = 'H'
        elif element == '001000':
            binary[n] = 'I'
        elif element == '001001':
            binary[n] = 'J'
        elif element == '001010':
            binary[n] = 'K'
        elif element == '001011':
            binary[n] = 'L'
        elif element == '001100':
            binary[n] = 'M'
        elif element == '001101':
            binary[n] = 'N'
        elif element == '001110':
            binary[n] = 'O'
        elif element == '001111':
            binary[n] = 'P'
        elif element == '010000':
            binary[n] = 'Q'
        elif element == '010001':
            binary[n] = 'R'
        elif element == '010010':
            binary[n] = 'S'
        elif element == '010011':
            binary[n] = 'T'
        elif element == '010100':
            binary[n] = 'U'
        elif element == '010101':
            binary[n] = 'V'
        elif element == '010110':
            binary[n] = 'W'
        elif element == '010111':
            binary[n] = 'X'
        elif element == '011000':
            binary[n] = 'Y'
        elif element == '011001':
            binary[n] = 'Z'
        elif element == '011010':
            binary[n] = 'a'
        elif element == '011011':
            binary[n] = 'b'
        elif element == '011100':
            binary[n] = 'c'
        elif element == '011101':
            binary[n] = 'd'
        elif element == '011110':
            binary[n] = 'e'
        elif element == '011111':
            binary[n] = 'f'
        elif element == '100000':
            binary[n] = 'g'
        elif element == '100001':
            binary[n] = 'h'
        elif element == '100010':
            binary[n] = 'i'
        elif element == '100011':
            binary[n] = 'j'
        elif element == '100100':
            binary[n] = 'k'
        elif element == '100101':
            binary[n] = 'l'
        elif element == '100110':
            binary[n] = 'm'
        elif element == '100111':
            binary[n] = 'n'
        elif element == '101000':
            binary[n] = 'o'
        elif element == '101001':
            binary[n] = 'p'
        elif element == '101010':
            binary[n] = 'q'
        elif element == '101011':
            binary[n] = 'r'
        elif element == '101100':
            binary[n] = 's'
        elif element == '101101':
            binary[n] = 't'
        elif element == '101110':
            binary[n] = 'u'
        elif element == '101111':
            binary[n] = 'v'
        elif element == '110000':
            binary[n] = 'w'
        elif element == '110001':
            binary[n] = 'x'
        elif element == '110010':
            binary[n] = 'y'
        elif element == '110011':
            binary[n] = 'z'
        elif element == '110100':
            binary[n] = '0'
        elif element == '110101':
            binary[n] = '1'
        elif element == '110110':
            binary[n] = '2'
        elif element == '110111':
            binary[n] = '3'
        elif element == '111000':
            binary[n] = '4'
        elif element == '111001':
            binary[n] = '5'
        elif element == '111010':
            binary[n] = '6'
        elif element == '111011':
            binary[n] = '7'
        elif element == '111100':
            binary[n] = '8'
        elif element == '111101':
            binary[n] = '9'
        elif element == '111110':
            binary[n] = '+'
        elif element == '111111':
            binary[n] = '/'
    print(''.join(binary))

if __name__ == "__main__":
    binary2base64(hex2binary(hex_string))


