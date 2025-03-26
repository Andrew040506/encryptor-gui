import tkinter as tk
import string
import Substitution
import Encryption
import Decryption


def update_gui(*args):
    method = method_var.get()

    shift_frame.grid_remove()
    substitution_frame.grid_remove()

    if method == "shift cipher":
        shift_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")
    elif method == "substitution cipher":
        substitution_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")


def shift_cipher(message, shift, mode):
    lista = list(string.ascii_uppercase + "0123456789!@#$%^&*()-=_+[]\{}|;':,./\"<>? ")

    if mode == "Encrypt":
        return Encryption.encrypt(message, shift, lista)
    elif mode == "Decrypt":
        return Decryption.decrypt(message, shift, lista)


def process_text():
    text = message_text.get("1.0", "end-1c")
    mode = mode_var.get()
    method = method_var.get()
    output = ""
    if method == "shift cipher":
        shift = shift_entry.get().strip()
        if not shift.isdigit():
            output_real_label.config(text="Error: the shift must be a positive integer", fg="red")
            return
        shift = int(shift)
        output = shift_cipher(text, shift, mode)
    elif method == "substitution cipher":
        output = "Substitution processing not implemented yet."

    output_real_label.config(text=f"{output}", fg="blue")


def copy_to_clipboard():
    text = output_real_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()


root = tk.Tk()
root.geometry("400x500")

# Make the columns expandable to center elements
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Main UI components
message_label = tk.Label(root, text="Message to encrypt", pady=10)
message_label.grid(row=1, column=0, columnspan=2, pady=5)

message_text = tk.Text(root, height=4, width=25)
message_text.grid(row=2, column=0, columnspan=2, pady=5)

mode_var = tk.StringVar(value="Encrypt")
method_var = tk.StringVar(value="shift cipher")

method_label = tk.Label(root, text="Encryption method")
method_label.grid(row=3, column=0, pady=5, columnspan=1)

method_menu = tk.OptionMenu(root, method_var, "shift cipher", "substitution cipher")
method_menu.grid(row=3, column=1, columnspan=1, pady=5)

shift_frame = tk.Frame(root)
shift_label = tk.Label(shift_frame, text="Shift")
shift_entry = tk.Entry(shift_frame)
shift_label.pack()
shift_entry.pack()

substitution_frame = tk.Frame(root)
substitution_label = tk.Label(substitution_frame, text="Substitution key (A-Z)")
substitution_label.pack()

process_button = tk.Button(root, text="Encrypt/Decrypt", command=process_text)
process_button.grid(row=6, column=0, columnspan=2, pady=10)

output_label = tk.Label(root, text="Output")
output_label.grid(row=7, column=0, columnspan=2, pady=5)

output_real_label = tk.Label(root, text="(output goes here)")
output_real_label.grid(row=8, column=0, columnspan=2, pady=5)

copy_button = tk.Button(root, text="Copy to clipboard", command=copy_to_clipboard)
copy_button.grid(row=9, column=0, columnspan=2, pady=10)

encrypt_radio_button = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt")
decrypt_radio_button = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt")
encrypt_radio_button.grid(row=0, column=0)
decrypt_radio_button.grid(row=0, column=1)

method_var.trace_add("write", update_gui)

update_gui()

root.mainloop()
