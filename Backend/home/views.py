from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import *

@login_required(login_url='login')
def home_page(request):
    user = request.user

    context = {
        'repos' : []
    }


    for i in Repository.objects.all():
        context['repos'].append(i)

   

    return render(request, 'index.html', context)



def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request=request, username=username, password=password)

    if user is not None:
        login(request, user=user)
        return redirect('home-page')


    return render(request, 'login-page.html')


def logout_page(request):
    logout(request)

    return redirect('login')