from hashlib import sha256

a= input("Enter the message: ").encode()
hash_object = sha256(a)
print(f"SHA-256 Hash: {hash_object.hexdigest()}")
