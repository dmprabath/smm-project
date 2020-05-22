from django.shortcuts import render, redirect, get_object_or_404
from quotations.models import Quotation
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def account(request):
    quotation = Quotation.objects
    return render(request, 'account.html', {'quotations': quotation})


@login_required(login_url='login')
def details(request, quot_id):
    quot = get_object_or_404(Quotation, pk=quot_id)
    return render(request, 'details.html', {'quot': quot})


def login(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('account')
        else:
            return render(request, 'login.html', {'error': 'User name or Password is invalid'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
