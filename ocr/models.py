from django.db import models

class OCRData(models.Model):
    image_name = models.CharField(max_length=255)
    extracted_text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
