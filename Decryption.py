import string
#from enum import nonmember
lista = list(string.ascii_uppercase + "0123456789")




# This is for the process of encrypting.
def decrypt(message, shift):
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
                new_index = locate_index - shift

            else:
                new_index = locate_index - shift


            try:
                cipher = lista[new_index]
                ciphertext.append(cipher)
            except IndexError:
                new_index = (locate_index - shift) % 36
                if new_index == 36:
                    new_index = 0
                cipher = lista[new_index]
                ciphertext.append(cipher)



        counter += 1


    formatted_string = "".join(ciphertext)
    print(formatted_string)

def main():
    while True:
        try:
            message = input("\nEnter a message to decrypt: ")
            shift = int(input("Enter the shift: "))
            decrypt(message, shift)
        except ValueError:
            print("Input Error: Numbers only!")



main()






