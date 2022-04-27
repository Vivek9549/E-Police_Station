from ast import Pass
from re import sub
from django.shortcuts import render,redirect
from django.http import HttpResponse

from Inspector.models import Ins, Sub
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

def admin_view_FIR(request):
    adm = Admin.objects.get(email=request.session['email'])
    FIRs= FIR.objects.all()
    return render(request,'admin-view-FIR.html',{'adm':adm,'FIRs':FIRs})

def admin_view_one_FIR(request,pk):
    adm = Admin.objects.get(email=request.session['email'])
    fir=FIR.objects.get(id=pk)
    return render(request, 'admin-view-one-FIR.html',{'adm':adm,'fir':fir})

def admin_station(request):
    adm = Admin.objects.get(email=request.session['email'])
    stations= Station.objects.all()
    return render(request, 'admin-station.html',{'adm':adm,'stations':stations})

def admin_one_station(request,pk):
    adm = Admin.objects.get(email=request.session['email'])
    stations= Station.objects.get(id=pk)
    if request.method == 'POST':
        stations.station = request.POST['station']
        stations.address = request.POST['address']
        if 'img' in request.FILES:
            stations.img = request.FILES['img']
        
        stations.save()
    return render(request, 'admin-one-station.html',{'adm':adm,'stations':stations})

def admin_user(request):
    adm = Admin.objects.get(email=request.session['email'])
    uid=User.objects.all()
    return render(request,'admin-user.html',{'adm':adm,'uid':uid})

def admin_one_user(request,pk):
    adm = Admin.objects.get(email=request.session['email'])
    uid = User.objects.get(id=pk)
    if request.method == 'POST':
        uid.fname = request.POST['fname']
        uid.lname = request.POST['lname']
        uid.phone = request.POST['phone']
        
        
        uid.save()
    return render(request, 'admin-one-user.html',{'adm':adm,'uid':uid})

def admin_inspector(request):
    adm = Admin.objects.get(email=request.session['email'])
    ins= Ins.objects.all()
    return render(request,'admin-inspector.html',{'adm':adm,'ins':ins})

def admin_one_ins(request,pk):
    adm = Admin.objects.get(email=request.session['email'])
    ins = Ins.objects.get(id=pk)
    if request.method == 'POST':
        ins.fname = request.POST['fname']
        ins.lname = request.POST['lname']
        ins.user_id = request.POST['user_id']
        if 'pic' in request.FILES:
            ins.pic = request.FILES['pic']
        
        ins.save()
    return render(request, 'admin-one-ins.html',{'adm':adm,'ins':ins})

def admin_subins(request):
    adm = Admin.objects.get(email=request.session['email'])
    sub= Sub.objects.all()
    return render(request,'admin-sub.html',{'adm':adm,'sub':sub})






