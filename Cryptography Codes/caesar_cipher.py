# Function to encrypt the text
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) + shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift_amount - 97) % 26 + 97)
            encrypted_text += new_char
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text

# Function to decrypt the text
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program flow
if __name__ == "__main__":
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift (key): "))
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    
    elif choice == 'd':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift (key): "))
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    
    else:
        print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")
# -----------------------------------------------------------
# OUTPUT: 

# Do you want to (E)ncrypt or (D)ecrypt? D
# Enter the message to decrypt: LEWLYPUJLPZHNYLHAALHJOLY
# Enter the shift (key): 7
# Decrypted message: EXPERINCEISAGREATTEACHER

