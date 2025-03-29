#import string
#from enum import nonmember

# This is for the process of encrypting.
def encrypt(message, shift, lista):
    ciphertext = []
    counter = 0
    formatted_message = message.upper()

    for x in range(len(message)):
        #Get each letter in message
        per_letter = formatted_message[counter]


        if per_letter not in lista:
            ciphertext.append(per_letter)
        else:
            locate_index = lista.index(per_letter)

            if shift < 0:
                new_index = locate_index + shift

            else:
                new_index = locate_index + shift


            try:
                cipher = lista[new_index]
                ciphertext.append(cipher)
            except IndexError:
                new_index = (locate_index + shift) % len(lista)
                if new_index == len(lista):
                    new_index = 0
                cipher = lista[new_index]
                ciphertext.append(cipher)
        counter += 1
    formatted_string = "".join(ciphertext)
    #much_formatted = formatted_string.replace(" ", "")
    return formatted_string

"""
def main():
    while True:
        try:
            message = input("\nEnter a message to encrypt: ")
            shift = int(input("Enter the shift: "))
            encrypt(message, shift)
        except ValueError:
            print("Input Error: Numbers only!")

"""

#main()






