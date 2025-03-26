import Encryption
import Decryption
from Decryption import decrypt
from Encryption import encrypt

def main():
    MJ_Cipher = input("Create your own cipher key: ")

    key = list(MJ_Cipher)
    formatted_key = [item.upper() for item in key]


    while True:
        print("""Menu
    1. Encrypt
    2. Decrypt
    3. Exit\n""")

        choice = input("Enter choice: ")
        while True:
            try:
                shift = int(input("Enter shift: "))
                break
            except ValueError:
                print("\nInteger only")

        message = input("Enter your message: ")

        if choice == '1':
            encrypt(message, shift, formatted_key)
        elif choice == '2':
            decrypt(message, shift, formatted_key)
        elif choice == '3':
            print("Thank you for using MJ CIPHER")
            break
        else:
            print("\nChoice is not valid\n")

if __name__ == "__main__":
    main()