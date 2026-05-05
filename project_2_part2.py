from tkinter import *
from PIL import Image, ImageTk
import csv

# -------------------------
# Window setup
# -------------------------
root = Tk()
root.title("CCSU App")
root.geometry("750x600")
root.configure(bg='light blue')

# -------------------------
# Logo processing (transparent white)
# -------------------------
img = Image.open('logo1.png')

# Pillow>=10 compatibility
try:
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100, 100), Image.ANTIALIAS)

img = img.convert("RGBA")

data_img = img.getdata()
newData = []

for item in data_img:
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)

logo = ImageTk.PhotoImage(img)

logoLabel = Label(root, image=logo, bg='light blue')
logoLabel.place(x=20, y=20)

# -------------------------
# Load CSV data
# -------------------------
data = []

try:
    with open("examfile.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
except Exception as e:
    print("Error loading CSV:", e)

# -------------------------
# Output label
# -------------------------
lb = Label(root, justify="left", bg="light blue", anchor="w", font=("Arial", 10))
lb.place(x=200, y=150)

# -------------------------
# Button functions
# -------------------------
def calendar():
    result = ""
    for row in data:
        val = row.get("CalendarDate", "")
        if val:
            result += val + "\n"
    lb.config(text=result if result else "No Calendar data found.")

def building():
    result = ""
    for row in data:
        val = row.get("Buildings", "")
        if val:
            result += val + "\n"
    lb.config(text=result if result else "No Buildings data found.")

def faculty():
    result = ""
    for row in data:
        val = row.get("FacultyName", "")
        if val:
            result += val + "\n"
    lb.config(text=result if result else "No Faculty data found.")

# -------------------------
# Buttons (horizontal)
# -------------------------
button_frame = Frame(root, bg="light blue")
button_frame.place(x=180, y=80)

btn1 = Button(button_frame, text="Calendar", bg="light green", width=15, command=calendar)
btn1.pack(side=LEFT, padx=5)

btn2 = Button(button_frame, text="Buildings", bg="light green", width=15, command=building)
btn2.pack(side=LEFT, padx=5)

btn3 = Button(button_frame, text="Faculty", bg="light green", width=15, command=faculty)
btn3.pack(side=LEFT, padx=5)

# -------------------------
# Run app
# -------------------------
root.mainloop()