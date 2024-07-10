import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image
import pillow_heif
import os
import sys
import traceback
import re

# Register HEIF plugin
pillow_heif.register_heif_opener()

# Log file
LOG_FILE = "heic2jpg.log"

# Define the version number
VERSION = "1.0.0"

def log_message(message):
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")

def convert_heic_to_jpg(heic_path):
    try:
        jpg_path = os.path.splitext(heic_path)[0] + ".jpg"

        # Use pillow_heif to open the HEIC file
        heif_file = pillow_heif.open_heif(heic_path)
        img = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data, 
            "raw", 
            heif_file.mode, 
            heif_file.stride
        )

        # Convert to RGB and save as JPG
        img = img.convert("RGB")
        img.save(jpg_path, "JPEG")
        return jpg_path
    except Exception as e:
        log_message(f"Error converting {heic_path}: {e}")
        return None

def process_files(files):
    for file in files:
        file = file.strip('{}')  # Remove curly braces if present
        if file.lower().endswith(".heic"):
            jpg_file = convert_heic_to_jpg(file)
            if jpg_file:
                status_text.config(state=tk.NORMAL)
                status_text.insert('1.0', f"Converted:\n{file}\nTo:\n{jpg_file}\n\n")  # Insert at the beginning
                status_text.config(state=tk.DISABLED)
            else:
                status_text.config(state=tk.NORMAL)
                status_text.insert('1.0', f"Failed to convert {file}. Check log for details.\n\n")  # Insert at the beginning
                status_text.config(state=tk.DISABLED)
        else:
            status_text.config(state=tk.NORMAL)
            status_text.insert('1.0', f"Invalid file type: {file}. Please drop .heic files only.\n\n")  # Insert at the beginning
            status_text.config(state=tk.DISABLED)

def drop(event):
    # Use regular expression to split the file paths correctly
    files = re.findall(r'{[^}]+}|[^\s]+', event.data)
    process_files(files)

def show_help():
    help_text = (
        "HEIC 2 JPG Converter\n\n"
        "Usage:\n"
        "1. Drag and drop .heic files onto the application window.\n"
        "2. The files will be automatically converted to .jpg format.\n\n"
        "You can also drag and drop .heic files onto the executable to convert them.\n\n"
        "Author: Dan Poynor"
    )
    messagebox.showinfo("Help", help_text)

root = TkinterDnD.Tk()
root.title("HEIC 2 JPG Converter")

frame = tk.Frame(root, width=400, height=200, bg='white')
frame.pack_propagate(False)
frame.pack(expand=True, fill=tk.BOTH)

# Update the label to make the text bigger and more noticeable
label = tk.Label(frame, text="Drag and drop .heic files here", bg='white', font=('Helvetica', 16, 'bold'))
label.pack(expand=True)

# Add a label to display the version number and author information on one line
version_author_label = tk.Label(root, text=f"Version {VERSION} | Author: Dan Poynor", fg='grey', bg=root['bg'], font=('Helvetica', 8))
version_author_label.pack(side=tk.BOTTOM, anchor='e', padx=5, pady=2)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

status_text = tk.Text(root, height=10, bg='white', state=tk.DISABLED, yscrollcommand=scrollbar.set)
status_text.pack(expand=True, fill=tk.BOTH)
scrollbar.config(command=status_text.yview)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# Add a menu bar with a Help menu
menu_bar = tk.Menu(root)
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help", command=show_help)
menu_bar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu_bar)

# Check for command-line arguments
if len(sys.argv) > 1:
    process_files(sys.argv[1:])

root.mainloop()