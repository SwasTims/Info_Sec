def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result
plaintext = input("Enter your message: ")
shift = int(input("Enter the no. of shift you want: "))
ciphertext = caesar_cipher(plaintext, shift)
print(f"Ciphertext: {ciphertext}")