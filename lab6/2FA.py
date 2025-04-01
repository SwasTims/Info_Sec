import pyotp
import hashlib

# User database (now allows registration)
users = {}

# Function to register a new user
def register_user():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists! Try a different one.")
        return
    password = input("Enter a new password: ")
    
    # Hash the password and generate a secret key for OTP
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    secret = pyotp.random_base32()

    # Store user credentials
    users[username] = {"password": hashed_password, "secret": secret}
    print(f"User {username} registered successfully! Use this OTP secret key for authentication: {secret}")

# Function to authenticate user with password
def authenticate_password(username, password):
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if users[username]["password"] == hashed_password:
            return True
    return False

# Function to authenticate user with OTP
def authenticate_otp(username):
    totp = pyotp.TOTP(users[username]["secret"])
    otp = totp.now()
    print(f"Generated OTP: {otp}")  # Display OTP for testing (should be sent via SMS/email in real-world apps)
    user_otp = input("Enter the OTP: ")
    return totp.verify(user_otp)

# Main authentication function
def two_factor_auth():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if authenticate_password(username, password):
        print("Password verified!")
        if authenticate_otp(username):
            print("Two-Factor Authentication Successful!")
        else:
            print("OTP Verification Failed!")
    else:
        print("Incorrect Username or Password!")

# Menu for user interaction
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        two_factor_auth()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
