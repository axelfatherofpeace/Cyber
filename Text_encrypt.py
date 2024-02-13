
from cryptography.fernet import Fernet

def main():    
    key = Fernet.generate_key()
    f = Fernet(key)

    Str1 = input("Enter the Text to Encrypt:")
    encrypted_text = f.encrypt(Str1.encode())
    print(encrypted_text)
    print("Text Encrypted Successfully")

if __name__ == '__main__':
    main()