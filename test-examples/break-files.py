#Globals
hex_string = '0xBEEF'
key = 5555
username = "aaaaaaaa"
password = "11111111"

def keyCalc(a, b):
    result = (a+b) * 8
    print("(" + str(a) + " + " + str(b) + ") * 8 = " + str(result))
    return result


def gen_password(s):
    length = len(s["username"])
    tmpPass = ""
    for i in range(length):
        key = s["key"] % 128
        realKey = s["calcKey"] % 128
        print("key:", key)
        print("RK:", realKey)
        print("ord:", ord(s["username"][i]))
        v = key + ord(s["username"][i]) ^ realKey
        v = v - 19
        print("v:",v)
        tmpPass += chr(v)
    return tmpPass

def swapNames(s):
    tmp = s["username"]
    s["username"] = s["password"]
    s["password"] = tmp
    return s

if __name__ == '__main__':

    byte_as_int = int(hex_string, 16)

    print("Hex as int value: " + str(key + int(hex_string, 16)))

    realKey = keyCalc(key, (key + int(hex_string, 16)))

    testStruct = {
        "username": username,
        "password": password,
        "calcKey" : realKey,
        "key" : key
    }
    print("testStruct: ", testStruct)
    # testStruct = swapNames(testStruct)
    # print("testStruct: ", testStruct)

    answer = gen_password(testStruct)
    print(answer)