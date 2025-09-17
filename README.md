Mayank Text Editor

📖 Overview

Mayank Text Editor is a simple and lightweight text editing application built using Python’s Tkinter library. It provides essential text editing functionalities like creating new files, opening existing ones, saving content, and performing standard edit operations.

This project is ideal for learning Python GUI development and understanding how to handle file I/O in desktop applications.


---

✨ Features

📝 Create a new text document

📂 Open existing .txt or any file and display its contents

💾 Save the current text to a file

✂ Standard edit operations: Cut, Copy, Paste

ℹ About menu to display application information

📜 Resizable text area with scroll support



---

⚙ Installation

No special installation is required since Tkinter comes with Python by default.

Requirements

Python 3.x (latest recommended)

Tkinter (bundled with Python on most systems)


Run the program

python mayank_text_editor.py


---

🖥 Usage

File Menu

New → Clears the text area for a new document

Open → Opens a dialog to select and load a file

Save → Opens a dialog to save the current content

Exit → Closes the application


Edit Menu

Cut → Cuts the selected text

Copy → Copies the selected text

Paste → Pastes from the clipboard


Help Menu

About → Shows application information



---

🧩 Code Structure

new_file() → Clears the editor for new content
open_file() → Opens a dialog, reads a file, and loads content

save_file() → Opens a save dialog and writes editor content

show_about() → Displays app info dialog


GUI is built using Tkinter widgets:

Menu Bar (File, Edit, Help)

Text Area with scrollbar



---

🚀 Future Enhancements

🔄 Undo/Redo functionality

🔍 Find and Replace feature

⌨ Keyboard shortcuts for quick actions

🎨 Rich text formatting (fonts, colors)

🌍 Multi-language support



