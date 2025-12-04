def encrypt(string, key):
    string = string.upper()
    key = key % 26
    result = ""
    temp = []
    for letter in string:
        if (letter.isalpha()):
            ascii = ord(letter) + key
            if (ascii > 90):
                ascii = ascii - 26
            temp.append(ascii)

    for ascii in temp:
        result += chr(ascii)

    return result

def decrypt(string, key):
    string = string.upper()
    key = key % 26
    result = ""
    temp = []
    for letter in string:
        if (letter.isalpha()):
            ascii = ord(letter) - key
            if (ascii < 65):
                ascii = ascii + 26
            temp.append(ascii)

    for ascii in temp:
        result += chr(ascii)

    return result

string = "XYZ"
key = 3
print(encrypt(string, key))
print(decrypt("ABC", key))