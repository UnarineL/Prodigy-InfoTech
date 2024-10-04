# Task 1: Caesar Cipher Program

This Python program implements the Caesar Cipher algorithm, allowing users to encrypt and decrypt text by shifting the characters in the message. The program is designed to be user-friendly, with prompts guiding the user through the encryption and decryption process.

## Features

- **Encryption and Decryption**: The program can both encrypt and decrypt messages using a specified shift value, making it versatile for different use cases.

- **User Input**: Users can enter their own message and choose the shift value for the cipher, providing flexibility in how the cipher is applied.

## Prerequisites

- **Python 3.x** installed on your machine.

## Usage

1. **Run the Program**: Execute the script to start the Caesar Cipher program.

## bash
   python caesar_cipher.py

Select Action: Choose 'e' for encryption or 'd' for decryption when prompted.

Enter Message: Input the message you wish to process. This can include letters, numbers, and spaces.

Specify Shift: Enter the shift value for the Caesar Cipher. A positive shift value will encrypt the message, while a negative shift value will decrypt it.

View Result: The program displays the encrypted or decrypted message after processing.

## How It Works

The program iterates through each character in the input message.
For letters, it shifts them according to the specified shift value, wrapping around the alphabet if necessary.
Non-letter characters remain unchanged, ensuring that the structure of the message is preserved.
Example
Input:

Message: "Hello, World!"
Shift: 3
Output: "Khoor, Zruog!"

Input:

Message: "Khoor, Zruog!"
Shift: -3
Output: "Hello, World!"

## Developed By

This code was developed as part of my internship at Prodigy InfoTech, demonstrating basic encryption and decryption techniques using the Caesar Cipher.