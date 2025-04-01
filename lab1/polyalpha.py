def vigenere_cipher(text, key):
    result = ""
    key = key.lower()
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('a')
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char.lower()) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result
plaintext = input("Enter your message: ")
key = input("Enter the no. of keys: ")
ciphertext = vigenere_cipher(plaintext, key)
print(f"Ciphertext: {ciphertext}")
