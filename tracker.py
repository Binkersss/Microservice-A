import time
import threading
import json
from datetime import datetime
from pynput import mouse, keyboard

activity_log = []
log_file_path = "activity-log.json"

def log_activity():
    keystrokes = 0
    clicks = 0
    movements = 0

    def on_press(key):
        nonlocal keystrokes
        keystrokes += 1

    def on_click(x, y, button, pressed):
        nonlocal clicks
        if pressed:
            clicks += 1

    def on_move(x, y):
        nonlocal movements
        movements += 1

    keyboard_listener = keyboard.Listener(on_press=on_press)
    mouse_listener = mouse.Listener(on_click=on_click, on_move=on_move)

    keyboard_listener.start()
    mouse_listener.start()

    while True:
        time.sleep(1)
        if keystrokes > 0 or clicks > 0 or movements > 0:
            timestamp = datetime.utcnow().isoformat() + "Z"
            log_entry = {
                "timestamp": timestamp,
                "keystrokes": keystrokes,
                "clicks": clicks,
                "movements": movements  
            }
            activity_log.append(log_entry)

            with open(log_file_path, "w") as f:
                json.dump(activity_log, f, indent=2)

        keystrokes = 0
        clicks = 0
        movements = 0  

def start_tracker():
    thread = threading.Thread(target=log_activity, daemon=True)
    thread.start()
