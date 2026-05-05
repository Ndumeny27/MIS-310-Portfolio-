from tkinter import *
from PIL import Image, ImageTk

# Window setup
root = Tk()
root.title("CCSU Mobile App")
root.geometry("500x500")
root.resizable(False, False)  # Prevent resizing
root.configure(bg="light blue")

# Load and display logo
try:
    img = Image.open("logo1.png")
    img = img.resize((120, 120))
    logo = ImageTk.PhotoImage(img)

    logo_label = Label(root, image=logo, bg="light blue")
    logo_label.pack(pady=10)

    # Prevent garbage collection
    logo_label.image = logo

except Exception as e:
    print("Logo not found or error loading image:", e)

# Title label
title_label = Label(
    root,
    text="Welcome to CCSU Mobile App",
    font=("Arial", 16, "bold"),
    bg="light blue"
)
title_label.pack(pady=10)

# Example content
info_label = Label(
    root,
    text="Select an option below:",
    font=("Arial", 12),
    bg="light blue"
)
info_label.pack(pady=5)

# Example buttons
btn1 = Button(root, text="Calendar")
btn1.pack(pady=5)

btn2 = Button(root, text="Buildings")
btn2.pack(pady=5)

btn3 = Button(root, text="Courses")
btn3.pack(pady=5)

# Run application
root.mainloop()