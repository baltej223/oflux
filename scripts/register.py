import sys
import os
import requests
import json

args = sys.argv

if len(args) != 2:
    print("Usage: python register.py <username>")
    exit(1)

username = args[1]

# Registration API URL (replace with your actual URL)
url = "https://your-backend.com/api/register"

# Payload to send
payload = {
    "username": username
}

# Send registration request to backend
try:
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        uid = data.get("uid")
        if uid:
            # Save UID to auth/.my_uid
            if not os.path.exists('auth'):
                os.makedirs('auth')
            with open("auth/.my_uid", "w") as f:
                f.write(uid)

            # Update UID map
            uid_map_path = "scripts/uid_map.json"
            if os.path.exists(uid_map_path):
                with open(uid_map_path, "r") as f:
                    uid_map = json.load(f)
            else:
                uid_map = {}

            uid_map[username] = uid

            with open(uid_map_path, "w") as f:
                json.dump(uid_map, f, indent=4)

            print(f"Registered successfully. UID: {uid}")
        else:
            print("Registration failed: UID not returned.")
    else:
        print(f"Registration failed with status code {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error connecting to server: {e}")

