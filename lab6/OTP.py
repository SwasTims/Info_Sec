import pyotp
import time

# Generate a secret key
secret_key = pyotp.random_base32()

# Create OTP generator
totp = pyotp.TOTP(secret_key)

# Generate OTP
otp = totp.now()
print(f"Generated OTP: {otp}")

# Wait for user input to verify OTP
user_otp = input("Enter the OTP: ")

# Validate OTP
if totp.verify(user_otp):
    print(" OTP Verified Successfully!")
else:
    print("Invalid OTP!")
