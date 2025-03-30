import tkinter as tk
from tkinter import messagebox
import string
import MorseCodePy
import Encryption
import Decryption
import Gnilogo

class CipherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x500")
        self.root.title("Cipher app")

        self.intro_frame = tk.Frame(self.root)
        self.intro_title_label = tk.Label(self.intro_frame, text="MEOW", font=("Arial", 20), pady=10)
        self.start_button = tk.Button(self.intro_frame, text="Start", font=("Arial", 20), command=self.start_program)
        self.intro_title_label.grid(row=1, column=0, columnspan=2, pady=5)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self.message_label = tk.Label(self.main_frame, text="Message to encrypt", pady=10)
        self.message_label.grid(row=1, column=0, columnspan=2, pady=5)

        self.message_text = tk.Text(self.main_frame, height=4, width=25)
        self.message_text.grid(row=2, column=0, columnspan=2, pady=5)

        self.mode_var = tk.StringVar(value="Encrypt")
        self.method_var = tk.StringVar(value="Shift cipher")

        self.method_label = tk.Label(self.main_frame, text="Encryption method")
        self.method_label.grid(row=3, column=0, pady=5, columnspan=1)

        self.method_menu = tk.OptionMenu(self.main_frame, self.method_var, "Shift cipher", "Substitution cipher",
                                         "Morse code cipher")
        self.method_menu.grid(row=3, column=1, columnspan=1, pady=5)

        self.info_button = tk.Button(self.main_frame, text="info", command=self.show_info)
        self.info_button.grid(row=3, column=2, pady=5, columnspan=1)

        self.shift_frame = tk.Frame(self.main_frame)
        self.shift_label = tk.Label(self.shift_frame, text="Shift")
        self.shift_entry = tk.Entry(self.shift_frame)
        self.shift_label.pack()
        self.shift_entry.pack()

        self.substitution_frame = tk.Frame(self.main_frame)
        self.substitution_label = tk.Label(self.substitution_frame, text="Substitution key (A-Z)")
        self.substitution_entry = tk.Entry(self.substitution_frame)
        self.substitution_label.pack()
        self.substitution_entry.pack()

        self.process_button = tk.Button(self.main_frame, text="Encrypt/Decrypt", command=self.process_text)
        self.process_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.output_label = tk.Label(self.main_frame, text="Output")
        self.output_label.grid(row=7, column=0, columnspan=2, pady=5)

        self.output_real_label = tk.Label(self.main_frame, text="(output goes here)")
        self.output_real_label.grid(row=8, column=0, columnspan=2, pady=5)

        self.copy_button = tk.Button(self.main_frame, text="Copy to clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=9, column=0, columnspan=2, pady=10)

        self.encrypt_radio_button = tk.Radiobutton(self.main_frame, text="Encrypt", variable=self.mode_var,
                                                   value="Encrypt")
        self.decrypt_radio_button = tk.Radiobutton(self.main_frame, text="Decrypt", variable=self.mode_var,
                                                   value="Decrypt")
        self.encrypt_radio_button.grid(row=0, column=0)
        self.decrypt_radio_button.grid(row=0, column=1)

        self.method_var.trace_add("write", self.update_gui)
        self.update_gui()

        self.intro_frame.pack()

    def update_gui(self, *args):
        method = self.method_var.get()
        self.shift_frame.grid_remove()
        self.substitution_frame.grid_remove()
        if method == "Shift cipher":
            self.shift_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")
        elif method == "Substitution cipher":
            self.substitution_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")
        else:
            print("invalid method")

    def shift_cipher(self, message, shift, mode):
        lista = list(string.ascii_uppercase + "0123456789!@#$%^&*()-=_+[]{}|;':,./\\\"<>? ")
        if mode == "Encrypt":
            return Encryption.encrypt(message, shift, lista)
        elif mode == "Decrypt":
            return Decryption.decrypt(message, shift, lista)
        else:
            return "Invalid mode"

    def substitution_cipher(self, message, mode, formatted_key):
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

    def morse_cipher(self, message, mode):
        if mode == "Encrypt":
            return MorseCodePy.encode(message, language='english')
        elif mode == "Decrypt":
            return MorseCodePy.decode(message, language='english')
        else:
            return "Invalid mode"

    def process_text(self):
        text = self.message_text.get("1.0", "end-1c")
        mode = self.mode_var.get()
        method = self.method_var.get()
        output = ""
        if method == "Shift cipher":
            shift = self.shift_entry.get().strip()
            if not shift.isdigit():
                self.output_real_label.config(text="Error: the shift must be a positive integer", fg="red")
                return
            shift = int(shift)
            output = self.shift_cipher(text, shift, mode)
        elif method == "Substitution cipher":
            key_str = self.substitution_entry.get().strip().upper()
            key_list = list(key_str)
            if len(key_list) != 26 or not all(c.isalpha() for c in key_list) or len(set(key_list)) != 26:
                self.output_real_label.config(text="Error: Key must be a list of 26 unique letters.", fg="red")
                return
            output = self.substitution_cipher(text, mode, key_list)
        elif method == "Morse code cipher":
            output = self.morse_cipher(text, mode)
        self.output_real_label.config(text=f"{output}", fg="blue")

    def copy_to_clipboard(self):
        text = self.output_real_label.cget("text")
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()

    def start_program(self):
        self.intro_frame.pack_forget()
        self.main_frame.pack()

    def show_info(self):
        info_text = """A substitution cipher replaces each letter in the plaintext with a corresponding letter from a fixed key, creating a scrambled message that can only be decoded with the same key.

    A shift cipher, also known as a Caesar cipher, moves each letter forward or backward in the alphabet by a fixed number. For instance, with a shift of 3, 'HELLO' becomes 'KHOOR'. 

    Lastly, Morse code represents each letter using a series of dots and dashes, allowing messages to be transmitted as sound or light signals, such as 'HELLO' being encoded as '.... . .-.. .-.. ---'."""
        messagebox.showinfo("Cipher Information", info_text)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CipherApp()
    app.run()