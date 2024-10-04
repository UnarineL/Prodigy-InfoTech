# Image Encryption Tool

This Python program implements a simple image encryption tool using pixel manipulation techniques. The program can encrypt and decrypt images by performing basic mathematical operations on the pixel values. It is designed to be user-friendly, guiding users through the encryption and decryption processes with clear prompts.

## Features

- **Image Encryption**: Users can encrypt an image by applying a mathematical operation to each pixel value, effectively altering the image to protect its content.

- **Image Decryption**: The program can reverse the encryption process to restore the original image, allowing users to access their data securely.

- **User Input**: Users can specify the image file they wish to encrypt or decrypt, along with an encryption/decryption key for the process.

- **File Handling**: The program saves the encrypted and decrypted images to specified file paths, ensuring easy retrieval after processing.

## How It Works

- **Encrypt Image**: The program multiplies each pixel value by a key and then divides by the key plus one to create the encrypted image. This manipulation effectively scrambles the pixel data.

- **Decrypt Image**: The program reverses the encryption process by multiplying each pixel value by the key plus one and then dividing by the key. This allows users to recover the original image accurately.

## Prerequisites

- **Python 3.x** installed on your machine.
- Required libraries (e.g., `Pillow` for image processing). You can install it via `pip`:

## bash
  pip install Pillow

## Usage

Run the Program: Execute the script to start the Image Encryption program.

## bash

python image_encryption_tool.py

Select Action: Choose 'e' for encryption, 'd' for decryption, or 'q' to quit the program.

Encrypt Image:

Enter the encryption key when prompted.
Specify the location or URL of the image to be encrypted.
Decrypt Image:

Enter the decryption key when prompted.
Specify the location of the encrypted image.
View Results: The program saves and indicates the location of the encrypted and decrypted images after processing.

## Security Considerations
Choose a strong encryption key that is not easily guessable to enhance the security of your encrypted images.
Keep your keys secure, as losing them may result in the inability to decrypt your images.

## Developed By

This code was developed as part of my internship at Prodigy InfoTech, showcasing a basic approach to image encryption and decryption through pixel manipulation.