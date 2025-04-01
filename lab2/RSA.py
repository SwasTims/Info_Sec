from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
encrypted = cipher.encrypt(input("Enter the message to encrypt: ").encode())
print(f"Encrypted message: {encrypted}")

decipher = PKCS1_OAEP.new(RSA.import_key(private_key))
decrypted = decipher.decrypt(encrypted)
print(f"Decrypted message: {decrypted.decode()}")
 