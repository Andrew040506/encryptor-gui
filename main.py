import tkinter as tk
import string

lista = list(string.ascii_uppercase + "0123456789")

def shift_encrypt(message, shift) -> str:
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
                new_index = (locate_index + shift) % 36
                if new_index == 36:
                    new_index = 0
                cipher = lista[new_index]
                ciphertext.append(cipher)
        counter += 1
    formatted_string = "".join(ciphertext)
    #much_formatted = formatted_string.replace(" ", "")
    return formatted_string

def process_text():
    text = message_text.get("1.0", "end-1c")
    mode = mode_var.get()
    method = method_var.get()
    shift = int(shift_entry.get())

    if method == "shift cipher":
        print("shift cipher")
        output = shift_encrypt(text, shift)

        output_label.config(text=f"Result: {output}")



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








root.mainloop()