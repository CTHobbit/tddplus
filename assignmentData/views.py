from django.http import HttpResponse
from django.shortcuts import render
from urllib3._collections import HTTPHeaderDict



def home_page(request):
    return render(request, 'home.html', {
        'new_Assignment ID': request.POST.get('Assignment ID', ''),
    })