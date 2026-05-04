import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

# Function to browse and select a PDF file
def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt")]
    )
    if file_path:
        file_label.config(text=file_path)
        extract_text(file_path)

# Function to extract text from PDF
def extract_text(file_path):
    global extracted_text
    extracted_text = ""

    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted_text += page.extract_text()
    else:
        with open(file_path, "r") as file:
            extracted_text = file.read()

# Simple summarization (placeholder)
def generate_notes():
    if not extracted_text:
        messagebox.showwarning("Warning", "Please select a file first.")
        return