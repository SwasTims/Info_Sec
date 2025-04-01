from hashlib import md5

a = input("Enter the message: ").encode()
hash_obj = md5(a)
print(f"MD5 Hash: {hash_obj.hexdigest()}")
