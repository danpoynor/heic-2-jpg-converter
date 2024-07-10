import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image
import pillow_heif
import os
import traceback
import shlex  # Added to handle file names with spaces

# Register HEIF plugin
pillow_heif.register_heif_opener()

# Log file
LOG_FILE = "heic2jpg.log"

def log_message(message):
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")

def convert_heic_to_jpg(heic_path):
    try:
        jpg_path = os.path.splitext(heic_path)[0] + ".jpg"

        # Use Pillow to open the HEIC file
        img = Image.open(heic_path)

        # Convert to RGB and save as JPG
        img = img.convert("RGB")
        img.save(jpg_path, "JPEG")
        return jpg_path
    except Exception as e:
        log_message(f"Error converting {heic_path}: {e}")
        return None

def drop(event):
    files = shlex.split(event.data)  # Updated to handle file names with spaces
    for file in files:
        if file.lower().endswith(".heic"):
            jpg_file = convert_heic_to_jpg(file)
            if jpg_file:
                status_text.config(state=tk.NORMAL)
                status_text.insert(tk.END, f"Converted:\n{file}\nTo:\n{jpg_file}\n\n")
                status_text.config(state=tk.DISABLED)
            else:
                status_text.config(state=tk.NORMAL)
                status_text.insert(tk.END, f"Failed to convert {file}. Check log for details.\n\n")  # Updated error message
                status_text.config(state=tk.DISABLED)
        else:
            status_text.config(state=tk.NORMAL)
            status_text.insert(tk.END, f"Invalid file type: {file}. Please drop .heic files only.\n\n")  # Updated error message
            status_text.config(state=tk.DISABLED)

root = TkinterDnD.Tk()
root.title("HEIC to JPG Converter")

frame = tk.Frame(root, width=400, height=200, bg='white')
frame.pack_propagate(False)
frame.pack(expand=True, fill=tk.BOTH)

label = tk.Label(frame, text="Drag and drop .heic files here", bg='white')
label.pack(expand=True)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

status_text = tk.Text(root, height=10, bg='white', state=tk.DISABLED, yscrollcommand=scrollbar.set)
status_text.pack(expand=True, fill=tk.BOTH)
scrollbar.config(command=status_text.yview)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.mainloop()
