from django.http import HttpResponse
from django.shortcuts import render
from urllib3._collections import HTTPHeaderDict




def home_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['Assignment ID'])
    return render(request, 'home.html')    
                    
   