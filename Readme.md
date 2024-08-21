
# Assignment 1: OCR and Data Extraction

This Django application uses OCR to extract text from uploaded images and 
display the results.



## Installation

Install and Setup OCR Django with following Commands and Steps

- Run Xampp Sever for Apache and MySQL (port - 80, 3306)
- Username of Database (Default) : root
- Password of Database (Default) : "" (empty)
- Database Name : ocr_data

```bash
  git clone https://github.com/ParthBarse/django-assesment-task.git
  cd django-assesment-task
  pip install -r requirements
  python manage.py runserver 
  
  # open localhost:8000  url in browser 
```
Note: You have to install [tesseract](https://github.com/UB-Mannheim/tesseract/wiki) module (Kepp it on default Path)
## Screenshots

Home Page (Upload Image) :

![App Screenshot](https://raw.githubusercontent.com/ParthBarse/django-assesment-task/main/screenshots/ocr-demo-1.jpeg)


Home Page (Live Camera Image) :

![App Screenshot](https://raw.githubusercontent.com/ParthBarse/django-assesment-task/main/screenshots/ocr-demo-2.jpeg)

History Page (MySQL Database Stored Data) :

![App Screenshot](https://raw.githubusercontent.com/ParthBarse/django-assesment-task/main/screenshots/ocr-demo-3.jpeg)
## Frameworks and Libraries used
- Tailwindcss
- Django
- pytesseract
- Fpdf

## Features
- Upload image and get scanned text 
- Capture Like Image from Webcam and Scan text from it 
- Image Retake Functionality
- Text Download Option in form of Text and PDF Files     
- All OCR Text and Metadata is saved in MySQL and Showed in History Page
- Image is Not saved, it is directly processed in memory

