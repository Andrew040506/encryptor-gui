import tkinter as tk
import string



def shift_cipher(message, shift, mode):
    lista = list(string.ascii_uppercase + "0123456789!@#$%^&*()-=_+[]\{}|;':,./\"<>? ")
    ciphertext = []
    counter = 0
    formatted_message = message.upper()
    print("Mode: ", mode)
    if mode == "Encrypt":
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
                    if new_index == 36:
                        new_index = 0
                    cipher = lista[new_index]
                    ciphertext.append(cipher)
            counter += 1
        formatted_string = "".join(ciphertext)
        #much_formatted = formatted_string.replace(" ", "")
        return formatted_string
    elif mode == "Decrypt":
        for x in range(len(message)):
            # Get each letter in message
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
        return formatted_string


def process_text():
    text = message_text.get("1.0", "end-1c")
    mode = mode_var.get()
    method = method_var.get()

    shift = shift_entry.get().strip()

    if not shift.isdigit():
        output_real_label.config(text="Error: the shift must be a positive integer", fg="red")
        return
    else:
        shift = int(shift)

    if method == "shift cipher":
        print("shift cipher")
        output = shift_cipher(text, shift, mode)

        output_real_label.config(text=f"{output}", fg="blue")

def copy_to_clipboard():
    text = output_real_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

root = tk.Tk()
root.geometry("400x500")
message_label = tk.Label(root, text="Message to encrypt", pady=10)

message_text = tk.Text(root, height=4, width=25)
shift_entry = tk.Entry(root)

mode_var = tk.StringVar(value="Encrypt")
method_var = tk.StringVar(value="shift cipher")

method_label = tk.Label(root, text="Encryption method")
output_label = tk.Label(root, text="Output")
output_real_label = tk.Label(root, text="(output goes here)")
shift_label = tk.Label(root, text="Shift")

method_menu = tk.OptionMenu(root, method_var, "substitution", "shift cipher")

process_button = tk.Button(root, text="Encrypt/Decrypt",  command=process_text)
encrypt_radio_button = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt")
decrypt_radio_button = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt")
copy_button = tk.Button(root, text="Copy to clipboard",  command=copy_to_clipboard)


encrypt_radio_button.pack()
decrypt_radio_button.pack()
method_label.pack()
method_menu.pack()
shift_label.pack()
shift_entry.pack()
message_label.pack()
message_text.pack()
process_button.pack()
output_label.pack()
output_real_label.pack()
copy_button.pack()








root.mainloop()