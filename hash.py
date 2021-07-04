import hashlib
text=input("Enter Input :")
res = hashlib.md5(text.encode())
print("This is md5 Hash :",res.hexdigest())