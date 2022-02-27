from django.urls import path
from .views import Projects

urlpatterns = [
    path('Projects/', Projects.as_view()),
]