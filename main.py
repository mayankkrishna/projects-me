import tkinter as t
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

def new_file():
    text_area.delete(1.0, t.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", ".txt"), ("All files", ".*"), ("c file", ".c")])
    if file_path:
        with open(file_path, "r") as file:
            text_content = file.read()
            text_area.get(1.0, t.END)
            text_area.delete(1.0, t.END)
            text_area.insert(t.END, text_content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", ".*"),  ("c file", ".c")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, t.END))

def show_about():
    messagebox.showinfo("About", "Basic Text Editor\nBuilt by Mayank Krishna :)")

root = t.Tk()
root.title("Mayank Text Editor")

menu_bar = t.Menu(root)

# File menu
file_menu = t.Menu(menu_bar, tearoff=False)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = t.Menu(menu_bar, tearoff=False)
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help menu
help_menu = t.Menu(menu_bar, tearoff=False)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

text_area = ScrolledText(root, wrap=t.WORD, undo=True)
text_area.pack(expand=True, fill="both")

root.mainloop()