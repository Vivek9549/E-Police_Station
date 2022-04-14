from ast import Pass
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def admin_index(request):
    return render(request,'admin-header.html')

def admin_login(request):
    return render(request,'admin-login.html')

