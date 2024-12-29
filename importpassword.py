import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='backslashreplace').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("-" * 50)

for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8', errors='backslashreplace').split('\n')
        
        password_line = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        password = password_line[0] if password_line else "None"
        
        print("{:<30}| {:<}".format(i, password))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(i, "ERROR"))

input("Press Enter to exit...")
