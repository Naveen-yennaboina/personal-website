from django.views.generic import View, CreateView
from .models import Users


class Contact(CreateView):
    model = Users
    fields = ('name', 'email', 'contact_number', 'company_name', 'description')
    template_name = 'contact/Contact.html'


class Contact1(CreateView):
    model = Users
    fields = ('name', 'email', 'contact_number', 'company_name', 'description')
    template_name = 'contact/Contact1.html'
