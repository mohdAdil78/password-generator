import random
import string
import os

def generate_password(length, include_uppercase, include_digits, include_specials):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    specials = string.punctuation

    # Build the character pool
    character_pool = lowercase
    if include_uppercase:
        character_pool += uppercase
    if include_digits:
        character_pool += digits
    if include_specials:
        character_pool += specials

    # Ensure the character pool isn't empty
    if not character_pool:
        raise ValueError("No character types selected. Unable to generate a password.")

    # Generate a random password
    return ''.join(random.choice(character_pool) for _ in range(length))


def save_password(password, file_path="output/generated_passwords.txt"):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "a") as file:
        file.write(password + "\n")
