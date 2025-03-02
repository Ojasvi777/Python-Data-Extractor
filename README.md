# PDF License Data Extractor

## Overview
The **PDF License Data Extractor** is a Python script designed to extract structured information from **arms license documents** in **PDF format**. The extracted details include:

- **Licensee’s Name**
- **Father’s Name**
- **Present & Permanent Addresses**
- **Police Station**
- **License Validity (From - To)**
- **Weapon Details (Type, Bore, Serial Number)**

The extracted data is **automatically saved** in an **Excel file**, making it easy to review and manage.

## Features
- ✅ Extracts essential details from PDF documents.
- ✅ Saves extracted information to an **Excel file**.
- ✅ Supports multiple weapon details in a single entry.
- ✅ **Lightweight and easy to run** on any system with Python installed.
- ✅ Uses **OCR (Tesseract) and PDF processing libraries** for data extraction.

## Prerequisites
Before running the script, ensure you have the following installed:

### 1. Install Python (if not installed)
Download and install **Python 3.8+** from [python.org](https://www.python.org/downloads/).

### 2. Install Dependencies
Run the following command to install required Python libraries:
```bash
pip install -r requirements.txt
```

Ensure **Tesseract-OCR** is installed and added to your system’s PATH. Download it from:
[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

## How to Use

### 1. Clone or Download the Repository
```bash
git clone https://github.com/your-repo/pdf-license-extractor.git
cd pdf-license-extractor
```

### 2. Run the Script
```bash
python extract_license_data.py
```
- A file selection prompt will appear. Choose a **PDF file** to extract data from.
- The extracted details are **automatically saved** in an Excel file.

### 3. View Extracted Data
- The default output file is:
  ```
  extracted_data.xlsx
  ```
  located in the same directory as the script.

## Notes
- Ensure the **PDF is clear and properly formatted** for accurate extraction.
- If the script does not run, check **Python dependencies** and ensure **Tesseract-OCR** is correctly installed.
- Modify the script as needed to improve accuracy for specific document formats.

## License
This project is intended for **educational and non-commercial** use only.

