import tkinter as tk


mode_var = ""
method_var = ""
root = tk.Tk()
root.geometry("400x500")
message_label = tk.Label(root, text="Message to encrypt", pady=10)
message_entry = tk.Entry(root)

method_label = tk.Label(root, text="Encryption method")
output_label = tk.Label(root, text="Output")
output_real_label = tk.Label(root, text="(output goes here)")

method_menu = tk.OptionMenu(root, method_var, "substitution", "shift")

process_button = tk.Button(root, text="Encrypt/Decrypt")
encrypt_radio_button = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt")
decrypt_radio_button = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt")

encrypt_radio_button.pack()
decrypt_radio_button.pack()
method_label.pack()
method_menu.pack()
message_label.pack()
message_entry.pack()
process_button.pack()
output_label.pack()
output_real_label.pack()








root.mainloop()