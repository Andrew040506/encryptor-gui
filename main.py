import tkinter as tk
from tkinter import messagebox
import string
import MorseCodePy
import Encryption
import Decryption


def update_gui(*args):
    method = method_var.get()

    shift_frame.grid_remove()
    substitution_frame.grid_remove()

    if method == "Shift cipher":
        shift_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")
    elif method == "Substitution cipher":
        substitution_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")
    else:
        print("invalid method")


def shift_cipher(message, shift, mode):
    lista = list(string.ascii_uppercase + "0123456789!@#$%^&*()-=_+[]{}|;':,./\"<>? ")

    if mode == "Encrypt":
        return Encryption.encrypt(message, shift, lista)
    elif mode == "Decrypt":
        return Decryption.decrypt(message, shift, lista)
    else:
        return "Invalid mode"


def substitution_cipher(message, mode, formatted_key):
    alphabet = list(string.ascii_uppercase)
    message = message.upper()

    if mode == "Encrypt":
        mapping = {alphabet[i]: formatted_key[i] for i in range(26)}
    elif mode == "Decrypt":
        mapping = {formatted_key[i]: alphabet[i] for i in range(26)}
    else:
        return "Invalid mode"

    result = ""
    for char in message:
        if char in mapping:
            result += mapping[char]
        else:
            result += char

    return result


def morse_cipher(message, mode):
    if mode == "Encrypt":
        return MorseCodePy.encode(message, language='english')
    elif mode == "Decrypt":
        return MorseCodePy.decode(message, language='english')
    else:
        return "Invalid mode"


def process_text():
    text = message_text.get("1.0", "end-1c")
    mode = mode_var.get()
    method = method_var.get()
    output = ""
    if method == "Shift cipher":
        shift = shift_entry.get().strip()
        if not shift.isdigit():
            output_real_label.config(text="Error: the shift must be a positive integer", fg="red")
            return
        shift = int(shift)
        output = shift_cipher(text, shift, mode)
    elif method == "Substitution cipher":
        key_str = substitution_entry.get().strip().upper()
        key_list = list(key_str)

        if len(key_list) != 26 or not all(c.isalpha() for c in key_list) or len(set(key_list)) != 26:
            output_real_label.config(text="Error: Key must be a list of 26 unique letters.", fg="red")
            return
        print("Substitution", text, mode, key_list)
        output = substitution_cipher(text, mode, key_list)
    elif method == "Morse code cipher":
        output = morse_cipher(text, mode)

    output_real_label.config(text=f"{output}", fg="blue")


def copy_to_clipboard():
    text = output_real_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

def start_program():
    intro_frame.pack_forget()
    main_frame.pack()


def show_info():
    info_text = """A substitution cipher replaces each letter in the plaintext with a corresponding letter from a fixed key, creating a scrambled message that can only be decoded with the same key. For example, if 'A' maps to 'X' and 'B' maps to 'Y', the word 'HELLO' might become 'CZGGJ'. 
    
    A shift cipher, also known as a Caesar cipher, moves each letter forward or backward in the alphabet by a fixed number. For instance, with a shift of 3, 'HELLO' becomes 'KHOOR'. 
    
    Lastly, Morse code represents each letter using a series of dots and dashes, allowing messages to be transmitted as sound or light signals, such as 'HELLO' being encoded as '.... . .-.. .-.. ---'."""

    messagebox.showinfo("Cipher Information", info_text)

root = tk.Tk()
root.geometry("400x500")
root.title("Cipher app")


intro_frame = tk.Frame(root)
intro_title_label = tk.Label(intro_frame, text="MEOW", font=("Arial", 20), pady=10)
start_button = tk.Button(intro_frame, text="Start", font=("Arial", 20), command=start_program)
intro_title_label.grid(row=1, column=0, columnspan=2, pady=5)
start_button.grid(row=3, column=0, columnspan=2, pady=5)

main_frame = tk.Frame(root)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

message_label = tk.Label(main_frame, text="Message to encrypt", pady=10)
message_label.grid(row=1, column=0, columnspan=2, pady=5)

message_text = tk.Text(main_frame, height=4, width=25)
message_text.grid(row=2, column=0, columnspan=2, pady=5)

mode_var = tk.StringVar(value="Encrypt")
method_var = tk.StringVar(value="Shift cipher")

method_label = tk.Label(main_frame, text="Encryption method")
method_label.grid(row=3, column=0, pady=5, columnspan=1)

method_menu = tk.OptionMenu(main_frame, method_var, "Shift cipher", "Substitution cipher",  "Morse code cipher")
method_menu.grid(row=3, column=1, columnspan=1, pady=5)

info_button = tk.Button(main_frame, text="info", command=show_info)
info_button.grid(row=3, column=2, pady=5, columnspan=1)

shift_frame = tk.Frame(main_frame)
shift_label = tk.Label(shift_frame, text="Shift")
shift_entry = tk.Entry(shift_frame)
shift_label.pack()
shift_entry.pack()

substitution_frame = tk.Frame(main_frame)
substitution_label = tk.Label(substitution_frame, text="Substitution key (A-Z)")
substitution_entry = tk.Entry(substitution_frame)
substitution_label.pack()
substitution_entry.pack()

process_button = tk.Button(main_frame, text="Encrypt/Decrypt", command=process_text)
process_button.grid(row=6, column=0, columnspan=2, pady=10)

output_label = tk.Label(main_frame, text="Output")
output_label.grid(row=7, column=0, columnspan=2, pady=5)

output_real_label = tk.Label(main_frame, text="(output goes here)")
output_real_label.grid(row=8, column=0, columnspan=2, pady=5)

copy_button = tk.Button(main_frame, text="Copy to clipboard", command=copy_to_clipboard)
copy_button.grid(row=9, column=0, columnspan=2, pady=10)

encrypt_radio_button = tk.Radiobutton(main_frame, text="Encrypt", variable=mode_var, value="Encrypt")
decrypt_radio_button = tk.Radiobutton(main_frame, text="Decrypt", variable=mode_var, value="Decrypt")
encrypt_radio_button.grid(row=0, column=0)
decrypt_radio_button.grid(row=0, column=1)

method_var.trace_add("write", update_gui)
update_gui()


intro_frame.pack()

root.mainloop()

