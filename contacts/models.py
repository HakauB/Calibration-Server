import os
from django.db import models
from django.forms import ModelForm
from django.core.files.storage import FileSystemStorage
from django import forms
from django.contrib.auth.models import User
import uuid
from django.db import models
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.

fs = FileSystemStorage(location='jobs/processes')   # Calibration file location

class Contact(models.Model):

    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, default = 'Default_user')
    processed = models.BooleanField(default=False)

    def get_upload_path(instance, filename):
        return 'processing/' + str(instance.owner.email) + '/' + str(len(Contact.objects.all())+1) + '/' + filename

    cal_file = models.FileField(null = True, blank = True, upload_to = get_upload_path, storage = fs)
    calibration = models.CharField(max_length = 255,)
    comments = models.CharField(max_length = 255, default = 'No comments')

    def __str__(self):
        return str(self.id) + " " + str(self.owner.email) + " " + self.calibration + " " + self.cal_file.name

    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk': self.id})
