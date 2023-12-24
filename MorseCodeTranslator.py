import contextlib
from pynput import keyboard
import threading
import time

def on_press(key):
    global event_time
    with contextlib.suppress(AttributeError):
        if key == keyboard.Key.space:
            event_time = time.time()

def key_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Set the event_time to the current time
event_time = time.time()

# Create and start the thread
thread = threading.Thread(target=key_listener)
thread.start()

# Main program loop (you can add other functionality here)
try:
    while True:
        if time.time() - event_time < 0.5:  # Adjust the threshold as needed
            print(".", end='', flush=True)
        else:
            print("-", end='', flush=True)
        time.sleep(0.5)
except KeyboardInterrupt:
    # Stop the thread when the program is interrupted
    thread.join()
