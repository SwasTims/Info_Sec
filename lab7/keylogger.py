import psutil

# List of common keylogger process names
keyloggers = ["keylogger.exe", "winlogon.exe", "spyware.exe", "logkeys", "hooker"]

def detect_keylogger():
    print("Scanning for keyloggers...")

    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_name = process.info['name'].lower()
            if process_name in keyloggers:
                print(f"Alert! Suspicious keylogger detected: {process_name} (PID: {process.info['pid']})")
        except Exception as e:
            continue

detect_keylogger()
