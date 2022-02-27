from django.urls import path
from .views import Contact, Contact1

urlpatterns = [
    path('Contact/', Contact.as_view()),

    path('Contact1/', Contact1.as_view(), name='contact-info'),
]