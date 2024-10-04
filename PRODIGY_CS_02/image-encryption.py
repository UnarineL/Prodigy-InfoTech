from PIL import Image
import numpy as np

print("Image Security Program.")

def apply_encryption(img_path, cipher_key):
    img = Image.open(img_path)

    img_array = np.array(img)

    secured_img_array = (img_array * cipher_key) // (cipher_key + 1)

    secured_img = Image.fromarray(np.uint8(secured_img_array))

    # Save the encrypted image
    encrypted_img_path = "secure_image.png"
    secured_img.save(encrypted_img_path)
    print(f"Image encryption completed. Encrypted image saved at: {encrypted_img_path}")

def apply_decryption(encrypted_img_path, cipher_key):
    encrypted_img = Image.open(encrypted_img_path)

    encrypted_array = np.array(encrypted_img)

    decrypted_array = (encrypted_array * (cipher_key + 1)) // cipher_key

    decrypted_array = np.clip(decrypted_array, 0, 255)

    decrypted_img = Image.fromarray(np.uint8(decrypted_array))

    # Save the decrypted image
    decrypted_img_path = "restored_image.png"
    decrypted_img.save(decrypted_img_path)
    print(f"Image decryption completed. Decrypted image saved at: {decrypted_img_path}")

def main_program():
    while True:
        print("Choose 'e' to Encrypt an image, 'd' to Decrypt an image, or 'q' to quit the program.")
        user_choice = input("Your selection: ")

        if user_choice == 'e':
            encryption_process()
        elif user_choice == 'd':
            decryption_process()
        elif user_choice == 'q':
            print("Terminating the program.")
            break
        else:
            print("Invalid input. Please select 'e' for encryption, 'd' for decryption, or 'q' to quit.")

def encryption_process():
    cipher_key = int(input("Enter the encryption key: "))
    img_path = input("Provide the file path or URL of the image: ")

    try:
        apply_encryption(img_path, cipher_key)
    except FileNotFoundError:
        print("Error: Image not found. Please ensure the file path is correct.")

def decryption_process():
    cipher_key = int(input("Enter the decryption key: "))
    encrypted_img_path = input("Provide the file path of the encrypted image: ")

    try:
        apply_decryption(encrypted_img_path, cipher_key)
    except FileNotFoundError:
        print("Error: Encrypted image not found. Please check the file path.")

if __name__ == "__main__":
    main_program()
