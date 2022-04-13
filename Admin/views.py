from ast import Pass
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def admin_index(request):
    adi=Admin.objects.get(user_id=request.session['user_id'])
    return render(request,'admin-index.html',{'adi':adi})

def admin_login(request):
    if request.method == 'POST':
        try:
            adi=Admin.objects.get(user_id=request.POST['user_id'])
            if request.POST['password'] == adi.password:
                request.session['user_id'] = request.POST['user_id']
                return redirect('admin-index')
            return render(request,'admin-login.html',{'msg':'Incorrect Password'})
        except:
            msg = 'User ID not registered' 
            return render(request,'admin-login.html',{'msg':msg})
    return render(request,'admin-login.html')

def admin_logout(request):
    del request.session['user_id']
    return redirect('index')