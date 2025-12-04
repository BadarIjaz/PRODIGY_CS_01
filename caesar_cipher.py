def encrypt(text, shift):
    result = ""
    
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            # ord() gets ASCII, shift it, -65 brings it to 0-25 range, %26 wraps around, +65 back to ASCII
            result += chr((ord(char) + shift - 65) % 26 + 65)
            
        # Encrypt lowercase characters
        elif char.islower():
            # Same logic but subtracting 97 for lowercase 'a'
            result += chr((ord(char) + shift - 97) % 26 + 97)
            
        # Keep numbers and symbols as they are
        else:
            result += char
            
    return result

def decrypt(text, shift):
    # Decryption is just encryption with a negative shift
    return encrypt(text, -shift)

def main():
    print("--- Caesar Cipher Program ---")
    while True:
        choice = input("\nDo you want to (e)ncrypt, (d)ecrypt, or (q)uit? ").lower()
        
        if choice == 'q':
            print("Exiting program.")
            break
            
        if choice in ['e', 'd']:
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter the shift value (e.g., 3): "))
                
                if choice == 'e':
                    encrypted_text = encrypt(message, shift)
                    print(f"\nEncrypted: {encrypted_text}")
                else:
                    decrypted_text = decrypt(message, shift)
                    print(f"\nDecrypted: {decrypted_text}")
            except ValueError:
                print("Invalid input. Please enter a number for the shift value.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()