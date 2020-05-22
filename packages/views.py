from django.shortcuts import render
from .models import Packages

# Create your views here.


def home(request):
    packages = Packages.objects
    return render(request, 'home.html', {'packages': packages})
