from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import UploadFileForm
from .models import Contact

# Create your views here.

from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.exceptions import PermissionDenied

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
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts-list')


class UpdateContactView(LoggedInMixin, ContactOwnerMixin, UpdateView):

    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')
