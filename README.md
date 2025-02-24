
PDF Data Extractor - Standalone Deployment
Overview
The PDF Data Extractor is a tool designed to extract structured information from arms license PDFs, including the licensee’s name, father’s name, addresses, police station, license validity, and weapon details. The extracted data is saved in an Excel file for easy reference. This application is available as a standalone executable, eliminating the need for any additional software installations.

Features
Extracts key details from PDFs automatically.

Stores extracted data in an Excel file.

Supports multiple weapon details in a single cell, separated by commas.

No Python or additional software required—just download and run.

How to Use
Download the EXE File

Get the latest version from GitHub Releases.

Run the Application

Double-click the .exe file.

A file selection dialog will appear.

Select a PDF file to extract details.

View Extracted Data

The extracted data will be automatically saved to an Excel file.

Default save location: C:\Users\aashish kathuria\Downloads\papaexcel.xlsx.

Deployment (For Developers)
To create the standalone executable:

pip install pyinstaller
pyinstaller --onefile --windowed script.py
--onefile: Packages everything into a single executable.

--windowed: Prevents a command prompt from opening.

The executable will be created inside the dist/ folder.

Notes
No installation required—simply download and run.

Ensure the PDF format follows a structured layout for accurate extraction.

If the application does not open, check Windows security settings or try running as Administrator.

License
This project is for educational and non-commercial use only.
