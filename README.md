# PDF Data Extractor - Standalone Deployment

## Overview
The **PDF Data Extractor** is a tool designed to extract structured information from arms license PDFs, including:
- Licensee’s Name
- Father’s Name
- Addresses (Present & Permanent)
- Police Station
- License Validity
- Weapon Details

The extracted data is saved in an Excel file for easy reference. This application is available as a **standalone executable**, eliminating the need for any additional software installations.

## Features
- ✅ Extracts key details from PDFs automatically.
- ✅ Stores extracted data in an Excel file.
- ✅ Supports multiple weapon details in a single cell, separated by commas.
- ✅ **No Python or additional software required**—just download and run.

## How to Use

### 1. Download the EXE File
- Get the latest version from [GitHub Releases](https://github.com/your-repo/releases).

### 2. Run the Application
- Double-click the `.exe` file.
- A file selection dialog will appear.
- Select a PDF file to extract details.

### 3. View Extracted Data
- The extracted data will be automatically saved in an Excel file.
- **Default save location:** `C:\Users\aashish kathuria\Downloads\papaexcel.xlsx`.

## Deployment (For Developers)
To create the standalone executable:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed script.py
