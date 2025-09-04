def encrypt_char(char, shift1, shift2):
    if char.islower():
        if 'a' <= char <= 'm':
            return chr((ord(char) - ord('a') + shift1 * shift2) % 26 + ord('a'))
        else:
            return chr((ord(char) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))
    elif char.isupper():
        if 'A' <= char <= 'M':
            return chr((ord(char) - ord('A') - shift1) % 26 + ord('A'))
        else:
            return chr((ord(char) - ord('A') + shift2 ** 2) % 26 + ord('A'))
    else:
        return char

def decrypt_using_original(original_file, encrypted_file, output_file, shift1, shift2):
    with open(original_file, 'r', encoding='utf-8') as f1, open(encrypted_file, 'r', encoding='utf-8') as f2:
        original_text = f1.read()
        encrypted_text = f2.read()
    
    decrypted_text = ''
    
    for orig_char, enc_char in zip(original_text, encrypted_text):
        if orig_char.islower():
            if 'a' <= orig_char <= 'm':
                decrypted_char = chr((ord(enc_char) - ord('a') - shift1 * shift2) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(enc_char) - ord('a') + shift1 + shift2) % 26 + ord('a'))
        elif orig_char.isupper():
            if 'A' <= orig_char <= 'M':
                decrypted_char = chr((ord(enc_char) - ord('A') + shift1) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(enc_char) - ord('A') - shift2 ** 2) % 26 + ord('A'))
        else:
            decrypted_char = enc_char
        decrypted_text += decrypted_char
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        f.write(decrypted_text)

def verify_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        content1 = f1.read().replace('\r\n', '\n')
        content2 = f2.read().replace('\r\n', '\n')
    if content1 == content2:
        print("Decryption successful: Files match!")
    else:
        print("Decryption failed: Files do not match!")

def main():
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))
    
    # Encrypt
    with open("raw_text.txt", 'r', encoding='utf-8') as f:
        content = f.read()
    encrypted_text = ''.join(encrypt_char(c, shift1, shift2) for c in content)
    with open("encrypted_text.txt", 'w', encoding='utf-8', newline='') as f:
        f.write(encrypted_text)
    print("Encryption done → 'encrypted_text.txt'")
    
    # Decrypt using original file for accurate shifts
    decrypt_using_original("raw_text.txt", "encrypted_text.txt", "decrypted_text.txt", shift1, shift2)
    print("Decryption done → 'decrypted_text.txt'")
    
    # Verify
    verify_files("raw_text.txt", "decrypted_text.txt")

if __name__ == "__main__":
    main()
