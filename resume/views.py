from django.shortcuts import render
from django.views.generic import View


class Resume(View):

    def get(self, request):
        return render(request, 'Resume/Resume.html')

