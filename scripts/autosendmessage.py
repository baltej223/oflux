import sys
import os
import json
import requests

# Usage: python scripts/autosendmessage.py <filename>

if len(sys.argv) != 2:
    print("Usage: python scripts/autosendmessage.py <filename>")
    exit(1)

filename = sys.argv[1]

# Validate file exists
if not os.path.exists(filename):
    print(f"File '{filename}' does not exist.")
    exit(1)

# Validate UID exists
uid_path = "scripts/auth/.my_uid"
if not os.path.exists(uid_path):
    print("UID not found. Please register first using register.py")
    exit(1)

with open(uid_path, "r") as f:
    sender_uid = f.read().strip()

# Get the receiver's username from the filename (e.g., "john.txt" -> "john")
receiver_username = os.path.splitext(os.path.basename(filename))[0]

# Read the last line (message) from the file
with open(filename, "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

# Only send if there is a new message
if not lines:
    print("No new message to send.")
    exit(0)

message = lines[-1]

# Prepend "You: " to the message
message = f"You: {message}"

# Get the receiver's UID from the uid_map
with open("scripts/uid_map.json", "r") as f:
    uid_map = json.load(f)

receiver_uid = uid_map.get(receiver_username)

if not receiver_uid:
    print(f"Receiver '{receiver_username}' not found in UID map.")
    exit(1)

# Send message to backend
payload = {
    "sender_uid": sender_uid,
    "receiver_uid": receiver_uid,
    "message": message
}

url = "https://your-backend.com/api/send-message"

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print(f"Message sent to {receiver_username}: {message}")
        # Append the message to the file
        with open(filename, "a") as f:
            f.write(f"\n{message}")
    else:
        print(f"Failed to send message: {response.status_code}")
        print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error sending message: {e}")

