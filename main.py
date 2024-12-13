from utils.password_generator import generate_password, save_password

def main():
    print("Welcome to Password Generator!")

    # Get user preferences
    try:
        length = int(input("Enter the desired password length: "))
        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        include_specials = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        # Generate the password
        password = generate_password(length, include_uppercase, include_digits, include_specials)

        # Display and save the password
        print(f"Generated Password: {password}")
        save_password(password)
    except ValueError:
        print("Invalid input. Please enter a number for the password length.")

if __name__ == "__main__":
    main()
