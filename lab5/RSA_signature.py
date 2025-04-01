from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

message = input("Enter your message: ").encode()
h = SHA256.new(message)

# Sign the message
signature = pkcs1_15.new(RSA.import_key(private_key)).sign(h)
print(f"Signature: {signature}")

# Verify the signature
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(h, signature)
    print("Signature valid")
except (ValueError, TypeError):
    print("Signature invalid")
    