from django.contrib import admin
from django.urls import include, path
from .views import homepage
from .views import download_text_view, download_pdf_view, ocr_view, ocr_history

urlpatterns = [
    # path("", homepage, name="homepage"),
    path('', ocr_view, name='home'),
    path('download_text/', download_text_view, name='download_text'),
    path('download_pdf/', download_pdf_view, name='download_pdf'),
    path('history/', ocr_history, name='ocr_history'),
]
