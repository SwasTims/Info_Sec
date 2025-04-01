from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a message
message = input("Enter your message: ").encode()
ciphertext = cipher.encrypt(message)
print(f"Ciphertext: {ciphertext}")

# Decrypt the message
decrypted_message = cipher.decrypt(ciphertext)
print(f"Decrypted message: {decrypted_message.decode()}")
