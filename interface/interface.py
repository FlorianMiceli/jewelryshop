import tkinter as tk
from tkinter import ttk
import random
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO

def displayData(tree, headers):
    tree["columns"] = headers
    for col in headers:
        tree.heading(col, text=col)

    tree.delete(*tree.get_children())

    rows = random.randint(3, 10)
    for r in range(rows):
        data = [f"{random.randint(1, 100)}" for _ in range(len(headers))]
        tree.insert("", "end", values=data)

def productsCatalog():
    frame = tk.Tk()
    frame.title("Fenêtre avec ListBox et tableaux")
    frame.iconphoto(False, tk_image)

    listbox_frame = tk.Frame(frame, bg="lightgray", width=200)
    listbox_frame.pack(side="left", fill="y")

    tab_frame = tk.Frame(frame, bg="white")
    tab_frame.pack(side="right", fill="both", expand=True)

    listbox = tk.Listbox(listbox_frame)
    listbox.pack(fill="both", expand=True)

    tables = [
        ["Header 1", "Header 2", "Header 3"],
        ["Header 1", "Header 2"],
        ["Header 1", "Header 2", "Header 3", "Header 4"],
        ["Header 1"],
        ["Header 1", "Header 2", "Header 3", "Header 4", "Header 5"]
    ]

    for i, headers in enumerate(tables):
        listbox.insert("end", f"Tableau {i+1}")

    tree = ttk.Treeview(tab_frame, show="headings")
    tree.pack(fill="both", expand=True)

    def on_listbox_select(event):
        index = listbox.curselection()[0]
        headers = tables[index]
        displayData(tree, headers)

    listbox.bind("<<ListboxSelect>>", on_listbox_select)

    frame.mainloop()

# Create a window for the main menu
root = tk.Tk()
root.geometry("800x600")
root.title("Menu principal")

# Create a frame for the title
title_frame = tk.Frame(root)
title_frame.pack(padx=10, pady=10)

# logo
url = "https://user-images.githubusercontent.com/103659071/234357295-4a152213-161e-4e9d-9bda-73d9d056dbde.jpg"
with urlopen(url) as u:
    raw_data = u.read()
image = Image.open(BytesIO(raw_data))
resized_image = image.resize((100, 100))
tk_image = ImageTk.PhotoImage(resized_image)
root.iconphoto(False, tk_image)
image_frame = tk.Frame(root)
image_frame.pack()

# Create a label widget inside the frame and pass the image to it
image_label = tk.Label(image_frame, image=tk_image)
image_label.pack()


# Add a title label to the frame
title_label = tk.Label(title_frame, text="Précieux Comptes Software")
title_label.config(font=("Copperplate Gothic Light", 20))
title_label.pack()

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=100, pady=100)

# Create a custom button style with the ttk module
style = ttk.Style()
style.configure("Custom.TButton", padding=10, relief="flat", background="#0078d7", foreground="black", font=("Helvetica", 12))

# Add a button to open the product catalog interface
table_button = ttk.Button(button_frame, text="Catalogue des produits", command=productsCatalog, style="Custom.TButton")
table_button.pack()

# Add other buttons for future sub-menus

# Launch the main window loop
root.mainloop()