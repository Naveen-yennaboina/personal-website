from django.db import models
from django.urls import reverse


class Users(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, unique=True)
    contact_number = models.CharField(max_length=100, unique=True)
    company_name = models.CharField(max_length=300)
    description = models.TextField(max_length=5000, null=True)

    def get_absolute_url(self):
        return reverse("contact-info")