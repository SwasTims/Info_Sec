from collections import defaultdict

# Sample log data (Simulating server logs)
log_data = """
192.168.1.1 - Failed login attempt
192.168.1.2 - Successful login
192.168.1.1 - Failed login attempt
192.168.1.1 - Failed login attempt
192.168.1.3 - Successful login
192.168.1.1 - Failed login attempt
192.168.1.1 - Failed login attempt
192.168.1.2 - Failed login attempt
"""

# Threshold for brute-force detection
BRUTE_FORCE_THRESHOLD = 3

# Function to detect brute-force attempts
def detect_brute_force(logs):
    login_attempts = defaultdict(int)
    for line in logs.split("\n"):
        if "Failed login attempt" in line:
            ip_address = line.split(" - ")[0]
            login_attempts[ip_address] += 1

            if login_attempts[ip_address] > BRUTE_FORCE_THRESHOLD:
                print(f"Alert! Possible brute-force attack detected from IP: {ip_address}")

# Run detection
detect_brute_force(log_data)
