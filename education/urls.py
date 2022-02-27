from django.urls import path
from .views import Education

urlpatterns = [
    path('Education/', Education.as_view()),
]