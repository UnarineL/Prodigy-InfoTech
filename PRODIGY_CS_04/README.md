# Simple Keylogger

This Python program implements a basic keylogger that records and logs keystrokes. It captures the keys pressed by the user and saves them to a log file, providing an educational tool for understanding how keylogging works. This program includes ethical considerations and requires user consent before running.

## Features

- **Key Logging**: Records and logs every keystroke along with a timestamp to provide context for each input.
- **Log File**: Saves the logged keystrokes to a specified file, allowing for easy review and analysis.
- **User Consent**: Includes a disclaimer and requires user acceptance of terms and conditions to ensure responsible usage.
- **Duration Control**: Allows the user to specify the duration for which the keystrokes should be logged, making it flexible for different use cases.

## Prerequisites

- **Python 3.x** installed on your machine.
- **pynput** library installed for keyboard monitoring. You can install it via pip:

## bash
  pip install pynput

## Usage

Run the Program: Execute the script to start the keylogger program.

## bash

python keylogger.py
Read and Accept Disclaimer: The program will display a disclaimer outlining the ethical use of the tool. Read the terms carefully and type y to accept and proceed.

Specify Duration: Enter the duration in seconds for which the keylogger should run. This will determine how long the program captures keystrokes.

Logging Keystrokes: During the specified duration, the program will capture and log all keystrokes made by the user.

Review Log: After the duration ends, the log file containing the keystrokes will be saved, and its location will be displayed on the screen for easy access.

## Ethical Considerations

This keylogger tool is intended solely for educational purposes. It is crucial to respect the privacy and consent of others when using this program. Always ensure you have explicit permission before running the keylogger on any device or network. The author is not responsible for any misuse of this tool.

## Developed By

This code was developed as part of my internship at Prodigy InfoTech, demonstrating the creation of a basic keylogger for educational purposes while emphasizing ethical usage and user consent.
