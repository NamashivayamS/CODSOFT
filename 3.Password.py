import random
import string

def generate_password(length, keyword, include_uppercase=True, include_digits=True, include_special_chars=True):
    if length < len(keyword):
        raise ValueError("Password length must be at least as long as the keyword.")
    
    characters = string.ascii_lowercase
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    extra_length = length - len(keyword)
    extra_characters = ''.join(random.choice(characters) for _ in range(extra_length))
    
    # Ensure keyword is included in the password
    password_parts = list(keyword) + list(extra_characters)
    random.shuffle(password_parts)
    
    return ''.join(password_parts)

def password_generator():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            keyword = input("Enter a keyword to include in the password: ").strip()
            if not keyword:
                print("Keyword cannot be empty. Please try again.")
                continue

            length = int(input("Enter the desired password length (minimum 4 characters): ").strip())
            if length < 4:
                print("Password length should be at least 4 characters for better security.")
                continue
            if length < len(keyword):
                print("Password length must be at least as long as the keyword you provided.")
                continue

            include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
            include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
            include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
            
            password = generate_password(length, keyword, include_uppercase, include_digits, include_special_chars)
            print(f"Your generated password: {password}")
        
        except ValueError as ve:
            print(f"Error: {ve}")
            continue
        
        cont = input("Would you like to generate another password? (yes to continue, any other key to exit): ").strip().lower()
        if cont != 'yes':
            print("Thanks for using the Password Generator! Stay safe and secure.")
            break

if __name__ == "__main__":
    password_generator()
