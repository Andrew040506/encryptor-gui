import tkinter as tk
from tkinter import ttk
from ascii_art_module import get_ascii_art
from welcome_ascii import get_welcome
#from animated_gif import AnimatedGIF

def display_ascii_line_by_line(window, text_widget, lines, index=0):
    if index < len(lines):
        text_widget.insert(tk.END, lines[index] + '\n')
        index += 1

        window.after(100, display_ascii_line_by_line, window, text_widget, lines, index)
    else:

        window.after(2000, switch_to_welcome, window)


def switch_to_welcome(window):

    window.destroy()

    welcome_window = tk.Tk()
    welcome_window.config(bg='black')
    welcome_window.attributes('-fullscreen', True)

    frame = tk.Frame(welcome_window, bg='blue')
    frame.pack(pady=20, padx=30)


    label = tk.Label(frame, text=get_welcome(), fg='white', bg='black')
    label.pack(pady=10)
    welcome_window.after(4000, lambda: [welcome_window.destroy()])
    welcome_window.mainloop()





def main():

    ascii_art = get_ascii_art()
    ascii_lines = ascii_art.strip().split('\n')


    intro_window = tk.Tk()
    intro_window.title("Intro with ASCII Art")
    intro_window.configure(bg="black")
    intro_window.attributes("-fullscreen", True)

    frame = tk.Frame(intro_window, bg='blue')
    frame.pack()



    text_widget = tk.Text(frame, height=44, width=150, bg="black", fg="white")
    text_widget.pack(pady=50    )




    display_ascii_line_by_line(frame, text_widget, ascii_lines)
    intro_window.after(8000, lambda: [intro_window.destroy()])
    intro_window.mainloop()


#if __name__ == "__main__":
main()
