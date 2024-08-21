import base64

import numpy as np
import pytesseract
from django.contrib import messages
from django.shortcuts import render
from PIL import Image
from fpdf import FPDF
from django.http import HttpResponse
from django.core.files.base import ContentFile
from pytesseract import image_to_string
from .models import OCRData


# you have to install tesseract module too from here - https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)


def homepage(request):
    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]
            # encode image to base64 string
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            messages.add_message(
                request, messages.ERROR, "No image selected or uploaded"
            )
            return render(request, "home.html")
        lang = "eng"
        img = np.array(Image.open(image))
        text = pytesseract.image_to_string(img, lang=lang)
        # return text to html
        return render(request, "home.html", {"ocr": text, "image": image_base64})

    return render(request, "home.html")

def download_text_view(request):
    text = request.GET.get('text', '')
    response = HttpResponse(text, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="extracted_text.txt"'
    return response

def download_pdf_view(request):
    text = request.GET.get('text', '')
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    response = HttpResponse(pdf.output(dest='S').encode('latin1'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="extracted_text.pdf"'
    return response

from io import BytesIO

def ocr_view(request):
    ocr_text = ""
    image_data = request.POST.get('image_data')
    image_name = None

    if image_data:
        # Process the base64 image data
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        image = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        # Convert to PIL Image
        image = Image.open(image)
        ocr_text = image_to_string(image)
        image_name = 'captured_image.' + ext

    elif 'imagefile' in request.FILES:
        # Process the uploaded image file
        image = request.FILES['imagefile']
        image_name = image.name
        image = Image.open(image)
        ocr_text = image_to_string(image)

    if ocr_text != "":
        # Save the OCR data to the database
        OCRData.objects.create(
            image_name=image_name,
            extracted_text=ocr_text,
        )

        return render(request, 'home.html', {
            'ocr': ocr_text,
        })
    else:
        return render(request, 'home.html', {
            'ocr': "No Text found in Image",
        })

def ocr_history(request):
    ocr_entries = OCRData.objects.all().order_by('-uploaded_at')
    return render(request, 'history.html', {'ocr_entries': ocr_entries})