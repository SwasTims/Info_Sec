from hashlib import sha256

hash_object = sha256(b'Hello World')
print(f"SHA-256 Hash: {hash_object.hexdigest()}")
