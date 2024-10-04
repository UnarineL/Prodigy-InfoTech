import re

def evaluate_password_strength(password):
    # Check each criterion
    contains_numbers = any(character.isdigit() for character in password)
    contains_uppercase = any(character.isupper() for character in password)
    contains_lowercase = any(character.islower() for character in password)
    is_length_sufficient = len(password) >= 8
    contains_special_chars = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Count how many criteria are satisfied
    criteria_count = sum([contains_numbers, contains_uppercase, contains_lowercase, is_length_sufficient, contains_special_chars])

    # Assess the password's strength
    if criteria_count == 5:
        return "Password Strength Level: Very Strong (Meets all 5 criteria)."
    elif criteria_count == 4:
        return "Password Strength Level: Strong (4 out of 5 criteria met)."
    elif criteria_count == 3:
        return "Password Strength Level: Moderate (3 out of 5 criteria met)."
    else:
        return "Password Strength Level: Weak (Fewer than 3 criteria met)."

def display_tips():
    print("----------------- Password Strength Checker -----------------")
    print("Follow these tips to improve your password security:")
    suggestions = [
        "1. Use at least 12 characters in your password.",
        "2. Include uppercase and lowercase letters, numbers, and special symbols.",
        "3. Avoid using common words or easily guessed information.",
        "4. Don't use personal details like your name, birthdate, or address.",
        "5. Consider using a passphrase made up of several unrelated words.",
        "6. Use a unique password for every account.",
        "7. Regularly update your passwords.",
        "8. Enable Two-Factor Authentication (2FA) for additional security.",
        "9. Be cautious of phishing scams; avoid entering your password on unfamiliar sites.",
        "10. Use a password manager to generate and store strong, unique passwords."
    ]
    for suggestion in suggestions:
        print(suggestion)

def main_program():
    display_tips()

    # Accept password input from user
    password = input("\nEnter the password you want to evaluate: ")

    # Masking password for output
    if len(password) > 2:
        hidden_password = password[0] + '#' * (len(password) - 2) + password[-1]
    else:
        hidden_password = password

    # Evaluate password strength
    strength = evaluate_password_strength(password)

    # Show masked password and strength evaluation
    print("\nYour Entered Password: {}".format(hidden_password))
    print("")
    print(strength)

if __name__ == "__main__":
    main_program()

