import sys
import os
import json
import websocket
import threading
import time

# Usage: python scripts/autoreceivemessage.py <filename>

if len(sys.argv) != 2:
    print("Usage: python scripts/autoreceivemessage.py <filename>")
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

# Get the receiver's UID from the uid_map
with open("scripts/uid_map.json", "r") as f:
    uid_map = json.load(f)

receiver_uid = uid_map.get(receiver_username)

if not receiver_uid:
    print(f"Receiver '{receiver_username}' not found in UID map.")
    exit(1)

# WebSocket callback functions
def on_message(ws, message):
    # Append new message to the file
    with open(filename, "a") as f:
        f.write(f"\n{message}")
    print(f"New message received and saved in {filename}: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### WebSocket connection closed ###")

def on_open(ws):
    print("### WebSocket connection opened ###")

    # Send an initial message to identify the user and start receiving messages
    # Backend should be listening for messages for this user
    payload = {
        "receiver_uid": receiver_uid
    }
    ws.send(json.dumps(payload))

# WebSocket URL (replace with your actual backend URL)
ws_url = "wss://your-backend.com/ws"

# Create a WebSocket connection
ws = websocket.WebSocketApp(
    ws_url,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
)

# Run the WebSocket in a separate thread
def run():
    ws.run_forever()

thread = threading.Thread(target=run)
thread.start()

# Keep the main thread alive while WebSocket is running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrupted by user.")
    ws.close()

