encoded_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

scale = 16
length = len(encoded_hex)
print(length)
num_of_bits = length * 4

binary_string = bin(int(encoded_hex, scale))[2:].zfill(num_of_bits)
print(binary_string)

for i in range(0, 256):
    bin_i =




#XOR binary_string with all different byte strings. Convert to ascii characters with binascii