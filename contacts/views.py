import os
import threading
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMessage
from django.core.files.base import ContentFile

# Create your views here.
from contacts.forms import UploadFileForm, CreateContactForm
from contacts.models import Contact

class ContactOwnerMixin(object):

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied

        return obj

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class ListContactView(LoggedInMixin, ListView):

    template_name = 'contact_list.html'
    model = Contact

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

class CreateContactView(LoggedInMixin, ContactOwnerMixin, CreateView):

    model = Contact
    template_name = 'edit_contact.html'
    form_class = CreateContactForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()

        def email_worker():
            msg = EmailMessage('Submission Received', 'You have submitted a file ' + obj.cal_file.name + '... wait a while', to=[str(obj.owner.email)])
            msg.send()
            folder = 'jobs/processes/processing/' + str(obj.owner.email) + '/' + str(obj.id) + '/'
            f = open(folder + 'calibration.conf', 'w')
            f.write(str(obj.cal_file.name) + '\n')
            f.write(str(obj.calibration) + '\n')
            f.write(str(obj.owner.email) + '\n')
            f.write(str(obj.comments) + '\n')
            f.close()

        threading.Thread(target = email_worker).start()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('contacts-list')

class UpdateContactView(LoggedInMixin, ContactOwnerMixin, UpdateView):

    model = Contact
    template_name = 'edit_contact.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts-list')
