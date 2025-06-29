import secrets
import string

def generate_password():
    while True:
        pw=int(input("Enter password length (minimum 8 characters): "))
        if pw < 8:
            print("Password length should be at least 8 characters.")
            continue
        else:
            break

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lowercase + uppercase + digits + symbols

    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    for _ in range(pw - 4):
        password_chars.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password_chars)
    password = ''.join(password_chars)
    print(f"Generated password: {password}")

def main():
    print("Welcome to the Password Generator!")
    while True:
        generate_password()
        cont = input("Do you want to generate another password? (yes to continue, no to quit): ").strip().lower()
        if cont == "no":
            print("Exiting password generator. Thank You! Come back again!")
            break

if __name__ == "__main__":
    main()