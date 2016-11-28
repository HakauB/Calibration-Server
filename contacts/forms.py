from django import forms
from .models import Contact
from django.db import models

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage

from captcha.fields import CaptchaField

fs = FileSystemStorage(location='/jobs/processes')

class UploadFileForm(forms.Form):
    model = Contact
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    email = EmailMessage('Hello', 'This is a test file', to=[])
'''
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
'''
