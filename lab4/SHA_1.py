from hashlib import sha1

a = input("Enter the message: ").encode()
hash_obj = sha1(a)
print(f"SHA-1 Hash: {hash_obj.hexdigest()}")
