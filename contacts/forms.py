from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.forms import ModelForm

from contacts.models import Contact

from registration.forms import RegistrationForm
from captcha.fields import CaptchaField

fs = FileSystemStorage(location='/jobs/processes')

class UploadFileForm(forms.Form):
    model = Contact
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class CreateContactForm(forms.ModelForm):

    cal_file = forms.FileField(required = True)
    calibration = forms.CharField(max_length = 255, required = True)
    comments = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ('cal_file', 'calibration', 'comments')

class CustomRegistrationForm(RegistrationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
