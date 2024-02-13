from cryptography.fernet import Fernet
import os
from cryptography.fernet import InvalidToken  
def generate_key():
    key = Fernet.generate_key()  #for generation of random key
    with open("Secret.key", "wb") as key_file:   #open file in write mode
        key_file.write(key)   #write the key into the file

def load_key():
    return open("Secret.key", "rb").read()  #open the secret key file in read mode

def encrypt(filename,key):
    f = Fernet(key)   #store key to f
    with open(filename, "rb") as file:               #open file to be encrypted in read mode
        file_data  = file.read()                #read file data
        encrypted_data = f.encrypt(file_data)                #store the encypted data to a temporary variable
    with open(filename, "wb") as file:          
        file.write(encrypted_data)              #write the encypted data


def decrypt(filename,key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except InvalidToken:
            print("Invalid key")
            return
    with open(filename, "wb") as file:
        file.write(decrypted_data)
                
                  
choice = input("Enter 'E' to Encrypt and 'D' for Decrypt :").upper() 
if choice == 'E':
    filename = input("Enter the file name with extension :")
    if os.path.exists(filename):
        generate_key()
        key=load_key()
        encrypt(filename,key)
        print("File Encrypted Successfully")
    else:
        print(f"file '{filename}' path not found !")

elif choice == 'D':
    filename = input("Enter the file name with extension :")
    if os.path.exists(filename):
        key=load_key()
        decrypt(filename,key)
        print("File Decrypted Successfully")
    else:
        print(f"file '{filename}' path not found !")

else:
    print("Invalid Choice")
                                     
