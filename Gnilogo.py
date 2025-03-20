import tkinter as tk
from tkinter import ttk
from ascii_art_module import get_ascii_art


def display_ascii_line_by_line(window, text_widget, lines, index=0):
    if index < len(lines):
        text_widget.insert(tk.END, lines[index] + '\n')
        index += 1

        window.after(100, display_ascii_line_by_line, window, text_widget, lines, index)
    else:

        window.after(1000, switch_to_main_menu, window)


def switch_to_main_menu(window):

    window.destroy()


    main_menu = tk.Tk()
    main_menu.title("Main Menu")
    main_menu.configure(bg="black")
    main_menu.attributes("-fullscreen", True)

    label = ttk.Label(main_menu, text="Welcome to MJ CIPHER", foreground="white", background="black")
    label.pack(pady=20)

    main_menu.mainloop()


def main():

    ascii_art = get_ascii_art()
    ascii_lines = ascii_art.strip().split('\n')


    intro_window = tk.Tk()
    intro_window.title("Intro with ASCII Art")
    intro_window.configure(bg="black")
    intro_window.attributes("-fullscreen", True)


    scrollbar = tk.Scrollbar(intro_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    text_widget = tk.Text(intro_window, height=44, width=150, bg="black", fg="white", yscrollcommand=scrollbar.set)
    text_widget.pack(pady=50    )

    scrollbar.config(command=text_widget.yview)


    display_ascii_line_by_line(intro_window, text_widget, ascii_lines)

    intro_window.mainloop()


if __name__ == "__main__":
    main()
