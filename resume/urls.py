from django.urls import path
from .views import Resume

urlpatterns = [
    path('Resume/', Resume.as_view()),
]