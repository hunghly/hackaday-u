
test_var = 'KeYpress'
hex_string = '0xDEADBEEFFACECAFE'

byte_as_int = int(hex_string, 16)
hex_value = hex(byte_as_int)

print("byte_as_int: ", byte_as_int)
print("hex_value: ", hex_value)
# print(ord(test_var[0]))
result = ""
for i in range (0,8):
    xor = (byte_as_int >> ((i << 3) & 0x3f))
    print("xor:", xor)
    # print("ch", chr(xor))
    # print((byte_as_int >> (i << 3) & 63) + ord(test_var[i]) + 1)
    # print(chr((byte_as_int >> (i << 3) & 63) + ord(test_var[i]) + 1))
    # print((byte_as_int >> (i << 3) & 63) + ord(test_var[i]) + 1)
    # print(chr((byte_as_int >> (i << 3) & 63) + ord(test_var[i]) + 1))
    # result = result + chr((byte_as_int >> ((i << 3) & 0x3f)) + ord(test_var[i]) + 1)
print("Result: ", result)



def byte(number, i):
    return (number & (0xff << (i * 8))) >> (i * 8)


XorMe = 0xDEADBEEFFACECAFE
globalVar = "KeYpress"
for i in range(8):
    print("byte((i << 3), 0) is ", byte((i << 3), 0))
    xor = XorMe >> (byte((i << 3), 0) & 0x3f)
    print("XOR:", xor)
    print("NV:", byte(xor + ord(globalVar[i]) + 1, 0))
    newValue = chr(byte(xor + ord(globalVar[i]) + 1, 0))
    #prints J0(kb$!R
    # print(newValue, end="")