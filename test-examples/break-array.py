
def get_password(keyword):
    password = ""
    for i in range(0, len(keyword)):
        current_ch = ord(keyword[i])
        if i == (len(keyword) - 1):
            next_ch = ord(keyword[0])
        else:
            next_ch = ord(keyword[i+1])
        if next_ch < current_ch:
            current_ch = current_ch - next_ch
        else:
            current_ch = next_ch - current_ch
        current_ch = current_ch + ord('`')
        password = password + chr(current_ch)
    return password

if __name__ == '__main__':
    array = ["hackadayu", "software", "reverse", "engineering", "ghidra"]
    passwords = []
    for keyword in array:
        password = get_password(keyword)
        passwords.append(password)
    print(passwords)