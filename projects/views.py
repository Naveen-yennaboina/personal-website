from django.shortcuts import render
from django.views.generic import View


class Projects(View):
    def get(self, request):
        return render(request ,'Projects/Projects.html')

