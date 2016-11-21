from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import UploadFileForm
from .models import Contact

# Create your views here.

from contacts.models import Contact

class ListContactView(ListView):

    template_name = 'contact_list.html'
    model = Contact

class CreateContactView(CreateView):

    model = Contact
    fields = '__all__'
    form = UploadFileForm()

    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')
