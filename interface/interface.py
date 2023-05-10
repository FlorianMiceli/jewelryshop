import tkinter as tk
from tkinter import ttk
import random
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO
from request import *

def displayData(tree, headers, data):
    tree["columns"] = headers
    for col in headers:
        tree.heading(col, text=col)

    tree.delete(*tree.get_children())

    for row in data:
        tree.insert("", "end", values=row)
        
    for col in headers:
        tree.column(col, width=10)

def productsCatalog():
    frame = tk.Tk()
    frame.title("Fenêtre avec ListBox et tableaux")
    frame.geometry("800x600")

    listbox_frame = tk.Frame(frame, bg="lightgray", width=200)
    listbox_frame.pack(side="left", fill="y")

    tab_frame = tk.Frame(frame, bg="white", width=600)
    tab_frame.pack(side="right", fill="both", expand=True)

    listbox = tk.Listbox(listbox_frame)
    listbox.pack(fill="both", expand=True)

    sub_menus = {
        "Chaines" : "select * from chaines;",
        "Perles" : "select * from perles;",
        "Colliers" : "select * from colliers;"
    }

    for title in sub_menus.keys():
        listbox.insert("end", title)

    tree = ttk.Treeview(tab_frame, show="headings")
    tree.pack(fill="both", expand=True)

    def on_listbox_select(event):
        sqlrequest = list(sub_menus.values())[listbox.curselection()[0]]
        headers = getHeaders(conn, sqlrequest)
        data = request(conn, sqlrequest)
        displayData(tree, headers, data)

    listbox.bind("<<ListboxSelect>>", on_listbox_select)

    frame.mainloop()

conn, tunnel = openConn()

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

closeConn(conn, tunnel)