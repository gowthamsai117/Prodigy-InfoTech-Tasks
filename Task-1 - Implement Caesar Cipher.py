def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? Enter 'E' or 'D' (or 'Q' to quit): ").upper()
        if choice == 'Q':
            break
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit.")
            continue

        text = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'E':
            encrypted_text = caesar_encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")
        else:
            decrypted_text = caesar_decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()