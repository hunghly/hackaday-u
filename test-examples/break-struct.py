def keyCalc(a, b):
    return (a+b) * 8


def gen_password(s):
    length = len(s["username"])
    print(length)
    tmpPass = ""
    for i in range(length):
        # print("a")
        # v = s["calcKey"] ^ s["key"] + ord(s["username"][i])
        v = (s["calcKey"] ^ s["key"]) + ord(s["password"][i])

        # print(ord(s["username"][i]))
        # print(v)
        v = v - 19
        print(v)
        tmpPass += hex(v)
        
    print(tmpPass)
    # tmpPassAsInt = int(tmpPass, 16)
    # hexValue = hex(tmpPass)
    # print(hexValue)
        
        

hex_string = '0xBEEF'

key = 12345
byte_as_int = int(hex_string, 16)



print("byte as int", byte_as_int)

print(key + int(hex_string, 16))

realKey = keyCalc(key, (key + int(hex_string, 16)))

print("Real Key: ", realKey)

sampleStruct = {
    "username": "abcdefgh",
    "password": "aaaaaaaa",
    "calcKey" : realKey,
    "key" : key
}

gen_password(sampleStruct)