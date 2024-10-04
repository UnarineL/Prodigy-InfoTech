print("Caesar Cipher Application!")

def caesar_cipher_process(input_text, shift_value, mode):
    final_result = ""
    for character in input_text:
        if character.isalpha():
            base = ord('a') if character.islower() else ord('A')
            shift_direction = shift_value if mode == 'encrypt' else -shift_value
            final_result += chr((ord(character) - base + shift_direction) % 26 + base)
        else:
            final_result += character
    return final_result

def run_program():
    operation = input("Choose an option: 'e' to encrypt or 'd' to decrypt: ").lower()
    while operation not in ['e', 'd']:
        print("Invalid choice! Please pick 'e' to encrypt or 'd' to decrypt.")
        operation = input("Choose an option: 'e' to encrypt or 'd' to decrypt: ").lower()

    text_input = input("Enter your message: ")
    shift_input = int(input("Provide the shift amount: "))

    mode = 'encrypt' if operation == 'e' else 'decrypt'
    processed_text = caesar_cipher_process(text_input, shift_input, mode)

    action_description = "Encrypted" if mode == 'encrypt' else "Decrypted"
    print(f"\n{action_description} Text: {processed_text}")

if __name__ == "__main__":
    run_program()
