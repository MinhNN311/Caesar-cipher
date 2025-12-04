def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_length = len(key)
    j = 0

    for char in plaintext:
        if char.isalpha():
            P = ord(char.upper()) - 65
            K = ord(key[j]) - 65
            C = (P + K) % 26
            ciphertext += chr(C + 65)
            j = (j + 1) % key_length
        else:
            ciphertext += char

    return ciphertext

# Example
plaintext = "RGZNFIBJWPE"
key = "XO"
ciphertext = vigenere_encrypt(plaintext, key)
print(ciphertext)
