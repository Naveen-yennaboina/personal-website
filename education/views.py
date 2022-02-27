from django.shortcuts import render
from django.views.generic import View


class Homepage(View):
    def get(self, request):
        return render(request, 'index.html')


class Education(View):
    def get(self, request):
        return render(request, 'Education/Education.html')
