import random
import string


def generate_password(length=12, use_letters=True, use_digits=True, use_special_chars=True):
    characters = ''

    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Invalid options. Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Password Generator")
    print("------------------")

    while True:
        print("\nOptions:")
        print("1. Generate Password")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            length = int(input("Enter the password length: "))
            use_letters = input("Include letters? (y/n): ").lower() == 'y'
            use_digits = input("Include digits? (y/n): ").lower() == 'y'
            use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

            password = generate_password(length, use_letters, use_digits, use_special_chars)
            print("\nGenerated Password:", password)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
