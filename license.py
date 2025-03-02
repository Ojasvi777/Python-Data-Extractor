import cv2
import pytesseract
import sqlite3
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, scrolledtext, Button, Label
import datetime

# Database Setup
db_file = "extracted_data.db"

def create_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS extracted_text (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        image_name TEXT,
                        extracted_text TEXT,
                        extracted_table TEXT,
                        extraction_time TEXT,
                        error_message TEXT)''')
    conn.commit()
    conn.close()

def save_to_db(image_name, text, table, error=None):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO extracted_text (image_name, extracted_text, extracted_table, extraction_time, error_message) 
                      VALUES (?, ?, ?, ?, ?)''', 
                   (image_name, text, table, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), error))
    conn.commit()
    conn.close()

def extract_text_from_image(image_path):
    try:
        # Read image
        image = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Adaptive thresholding
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

        # Remove noise
        kernel = np.ones((1, 1), np.uint8)
        processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # OCR text extraction
        custom_config = r'--oem 3 --psm 6'
        extracted_text = pytesseract.image_to_string(processed, config=custom_config)

        # Extract tabular data
        table_data = pytesseract.image_to_data(processed, output_type=pytesseract.Output.DATAFRAME)
        table_data_cleaned = table_data[['level', 'left', 'top', 'width', 'height', 'text']].dropna().to_string(index=False)

        # Save results
        save_to_db(image_path, extracted_text, table_data_cleaned)

        return extracted_text, table_data_cleaned, None  # No error
    except Exception as e:
        save_to_db(image_path, "", "", str(e))  # Save error
        return None, None, str(e)

# GUI for uploading and displaying results
def upload_and_process():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    text, table, error = extract_text_from_image(file_path)
    
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)  # Clear previous results
    
    if error:
        result_text.insert(tk.INSERT, f"⚠️ Error: {error}")
    else:
        result_text.insert(tk.INSERT, f"📄 Image Name: {file_path}\n")
        result_text.insert(tk.INSERT, f"⏳ Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        result_text.insert(tk.INSERT, f"📜 Extracted Text:\n{text}\n\n")
        result_text.insert(tk.INSERT, f"📊 Extracted Table:\n{table}\n\n")

    result_text.config(state=tk.DISABLED)

# Create GUI window
root = tk.Tk()
root.title("OCR Extractor")
root.geometry("800x600")

# Upload Button
upload_button = Button(root, text="📂 Upload Image", command=upload_and_process, font=("Arial", 14))
upload_button.pack(pady=10)

# Display Area
result_text = scrolledtext.ScrolledText(root, width=90, height=30, wrap=tk.WORD)
result_text.pack(padx=10, pady=10)
result_text.config(state=tk.DISABLED)

# Run the GUI
create_db()  # Ensure DB is set up
root.mainloop()
