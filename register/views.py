from typing import NoReturn
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import user_registration
# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def loginPage(request):
    if request.method == 'POST':
        email_l = request.POST.get('email')
        password_l = request.POST.get('password')

        user = authenticate(request, email = email_l,password = password_l)

        if user is not None:
            login(request,user)
            return redirect('show.html')
        else:
            messages.info(request,'email or password is incorrect')

    
    return render(request,'login.html')


def register(request):

    if request.method == 'POST':
        username_r = request.POST.get('username')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        c_password_r = request.POST.get('C_password')
        address_r = request.POST.get('address')
        if(password_r == c_password_r):
            messages.success(request,"Registration Successful")
            g= user_registration(username=username_r,email=email_r,
            password=password_r,c_password=c_password_r,address=address_r)
            g.save()
            return redirect('login')
        else:
            messages.success(request,"Incorrect Confirm Password TRY AGAIN!!")
            return render(request,'register.html')
            

    else:
        return render(request,'register.html')

    
def logoutuser(request):
    logout(request)
    return redirect('welcome.html')
    

def show(request):
    return render(request,'show.html')