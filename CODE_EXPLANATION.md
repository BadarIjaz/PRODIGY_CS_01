# Caesar Cipher: Code Analysis & Walkthrough

This document provides a technical deep-dive into the `caesar_cipher.py` implementation. It outlines the algorithmic logic, Python syntax, and design decisions used to secure the data.

## Core Concepts
To implement the cipher effectively, three key Python concepts were utilized:

1. **ASCII Conversion (`ord`)**: The `ord()` function converts a character into its integer ASCII value (e.g., `'A'` $\rightarrow$ `65`).
2. **Character Reconstruction (`chr`)**: The `chr()` function converts an integer back into a Unicode character.
3. **Modular Arithmetic (`%`)**: The modulo operator ensures the alphabet "wraps around." If a shift moves past 'Z', the algorithm cycles back to 'A'.

---

## Logic Breakdown

### 1. The Encryption Loop
The function iterates through the input message one character at a time.

```
def encrypt(text, shift):
    result = ""
    
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
result = "": We initialize an empty string to accumulate the encrypted characters.

for i in range(len(text)): A linear loop that processes the message from start to finish.

char = text[i]: Extracts the current character for processing.
```

---

### 2. The Mathematical Shift (Uppercase)
This single line encapsulates the core logic of the Caesar Cipher for capital letters.

    if char.isupper():
        result += chr((ord(char) + shift - 65) % 26 + 65)
        
Step-by-Step Execution:

char.isupper(): Verifies the character is A-Z.

ord(char) - 65: Normalizes the ASCII value to a 0-25 index (where A=0, B=1... Z=25).

+ shift: Applies the secret key (shift value) to the index.

% 26: Wraps the value within the alphabet range.

Example: Shifting 'Z' (25) by 1 results in 26. 26 % 26 = 0, returning us to 'A'.

+ 65: Converts the index back to the uppercase ASCII range.

chr(...): Converts the final integer back into a string character.

---

### 3. Handling Lowercase
The logic is identical to uppercase, but the ASCII offset differs.

    elif char.islower():
        result += chr((ord(char) + shift - 97) % 26 + 97)

Why 97?: This is the ASCII value for lowercase 'a'.

We subtract 97 to normalize 'a' to index 0, perform the shift, and add 97 back to return to the correct ASCII range.

---

### 4. Preserving Symbols

    else:
        result += char
        
Non-alphabetic characters (numbers, punctuation, spaces) are appended to the result without modification, ensuring sentence structure is preserved.

---

### 5. Efficient Decryption

```
def decrypt(text, shift):
    return encrypt(text, -shift)
```
Algorithmic Efficiency: Instead of rewriting the loop logic, we utilize the mathematical inverse.

Decrypting a shift of +N is mathematically identical to encrypting with -N.

---

### 6. Robust Error Handling
To prevent program crashes, user input is validated.

    try:
        shift = int(input("Enter the shift value: "))
        # ... logic ...
    except ValueError:
        print("Invalid input. Please enter a number.")
        
try...except ValueError: If a user enters text (e.g., "five") instead of an integer, the program catches the error and displays a friendly warning rather than terminating unexpectedly.

---

### 7. Execution Control

```
if __name__ == "__main__":
    main()
```
This standard Python conditional ensures the script runs the main() function only when executed directly, not when imported as a module.
