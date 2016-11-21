from django import forms
from .models import Contact
from django.db import models

from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/jobs/processes')

class UploadFileForm(forms.Form):
    model = Contact
    title = forms.CharField(max_length=50)
    file = forms.FileField()
