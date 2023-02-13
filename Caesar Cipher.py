#Caesar Cipher: Write a program that implements the Caesar cipher encryption technique.

def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_char = chr((ord(char.upper()) - 65 + shift) % 26 + 65)
            if char.islower():
                shift_char = shift_char.lower()
            ciphertext += shift_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_char = chr((ord(char.upper()) - 65 - shift) % 26 + 65)
            if char.islower():
                shift_char = shift_char.lower()
            plaintext += shift_char
        else:
            plaintext += char
    return plaintext

text = input("Enter a message: ")
shift = int(input("Enter a shift value: "))

encrypted_text = encrypt(text, shift)
print("Encrypted message:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted message:", decrypted_text)
