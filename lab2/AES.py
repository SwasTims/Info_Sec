from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Get user input for plaintext
plaintext = input("Enter the message to encrypt: ").encode()

# Generate a random 8-byte key
key = get_random_bytes(16)  # AES key must be 16, 24, or 32 bytes
cipher = AES.new(key, AES.MODE_CBC)

# Encrypt the message
padded_text = pad(plaintext, AES.block_size)
ciphertext = cipher.encrypt(padded_text)

# Display the encrypted message
print(f"Ciphertext: {ciphertext}")

# Decrypt
decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
decrypted_text = unpad(decipher.decrypt(ciphertext), AES.block_size)

# Display the decrypted message
print(f"Decrypted text: {decrypted_text.decode()}")
