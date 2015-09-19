import hexToBase64

original = '1c0111001f010100061a024b53535009181c'
xor = '686974207468652062756c6c277320657965'

originalBinary = hexToBase64.hex2binary(original)
xorBinary = hexToBase64.hex2binary(xor)

diff = len(xorBinary) - len(originalBinary)
originalBinary = '0' * diff + originalBinary

result = []
#for i in range(0, len(originalBinary)-1):
#   result[i] = int(originalBinary[i]) ^ int(xorBinary[i])

print(int(originalBinary[0]) ^ int(xorBinary[0]))
