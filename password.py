import hashlib

password = input("Enter the password: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()


if hashed_password == '1234':
    print("Access Granted")
   
else:
    print("Access Denied")

