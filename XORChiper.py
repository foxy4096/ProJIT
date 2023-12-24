def encrypt(text, key):
    encrypted_text = []
    for char in text:
        encrypted_char = chr(ord(char) ^ key)  # XOR each character with the key
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)

def decrypt(text, key):
    return encrypt(text, key)  # XORing twice with the same key decrypts the text

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            key = int(input("Enter the encryption key (an integer): "))
            encrypted_text = encrypt(text, key)
            print("Encrypted text:", encrypted_text)
        elif choice == "2":
            text = input("Enter the text to decrypt: ")
            key = int(input("Enter the decryption key (an integer): "))
            decrypted_text = decrypt(text, key)
            print("Decrypted text:", decrypted_text)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
