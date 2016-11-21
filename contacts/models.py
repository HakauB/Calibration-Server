from django.db import models
from django.core.files.storage import FileSystemStorage
from django import forms

# Create your models here.

fs = FileSystemStorage(location='jobs/processes')

class Contact(models.Model):

    cal_file = models.FileField(null = True, blank = True, upload_to = 'processing', storage = fs)

    email = models.EmailField()

    calibration = models.CharField(
        max_length = 255,
    )

    def __str__(self):
        return self.email + " " + self.calibration + " " + self.cal_file.name
