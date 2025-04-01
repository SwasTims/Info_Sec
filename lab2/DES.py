from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Get user input for plaintext
plaintext = input("Enter the message to encrypt: ").encode()

# Generate a random 8-byte key
key = get_random_bytes(8)  # DES key must be 8 bytes
cipher = DES.new(key, DES.MODE_CBC)

# Encrypt the message
padded_text = pad(plaintext, DES.block_size)
ciphertext = cipher.encrypt(padded_text)

# Display the encrypted message
print(f"\nCiphertext (hex): {ciphertext.hex()}")

# Decrypt the message
decipher = DES.new(key, DES.MODE_CBC, cipher.iv)
decrypted_text = unpad(decipher.decrypt(ciphertext), DES.block_size)

# Display the decrypted message
print(f"\nDecrypted text: {decrypted_text.decode()}")