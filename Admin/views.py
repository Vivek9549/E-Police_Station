from ast import Pass
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *

# Create your views here.

def admin_index(request):
    adm = Admin.objects.get(email=request.session['email'])
    return render(request,'admin-index.html',{'adm':adm})

def admin_login(request):
    if request.method == 'POST':
        try:
            adm = Admin.objects.get(email=request.POST['email'])
            if request.POST['password'] == adm.password:
                request.session['email'] = request.POST['email']
                return redirect('admin-index')
            return render(request,'admin-login.html',{'msg':'Incorrect Password'})
        except:
            msg = 'Account not registered' 
            return render(request,'admin-login.html',{'msg':msg})
    return render(request,'admin-login.html')

def admin_logout(request):
   del request.session['email']
   return redirect('index') 
