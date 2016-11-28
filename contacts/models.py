from django.db import models
from django.forms import ModelForm
from django.core.files.storage import FileSystemStorage
from django import forms
from django.contrib.auth.models import User
import uuid

# Create your models here.

fs = FileSystemStorage(location='jobs/processes')

class Contact(models.Model):

    id = models.AutoField(primary_key=True)

    cal_file = models.FileField(null = True, blank = True, upload_to = 'processing', storage = fs)

    calibration = models.CharField(
        max_length = 255,
    )

    owner = models.ForeignKey(User, default = 'Default_user')

    def __str__(self):
        return str(self.id) + " " + str(self.owner.email) + " " + self.calibration + " " + self.cal_file.name

    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk': self.id})

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['id', 'cal_file', 'calibration', 'owner']

    #def getEmail():
