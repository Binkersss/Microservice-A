import json
import os

def testMicroservice():
    log_file_path = "activity-log.json"

    if not os.path.exists(log_file_path):
        print("Log file not found. Has the tracker started running yet?")
        return

    try:
        with open(log_file_path, "r") as file:
            logs = json.load(file)

        print(f"Found {len(logs)} log entries:\n")
        for entry in logs:
            timestamp = entry.get("timestamp", "N/A")
            clicks = entry.get("clicks", 0)
            keystrokes = entry.get("keystrokes", 0)
            print(f"{timestamp} — Clicks: {clicks}, Keystrokes: {keystrokes}")

    except json.JSONDecodeError:
        print("Error: Log file is not in valid JSON format.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    testMicroservice()
