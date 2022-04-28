from ast import Pass
from re import sub
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Inspector.models import Ins

from myapp.models import FIR, Complaint, Station
from . models import *

# Create your views here.

def com_login(request):
    if request.method == 'POST':
        try:
            com = Com.objects.get(email=request.POST['email'])
            if request.POST['password'] == com.password:
                request.session['email'] = request.POST['email']
                return redirect('com-index')
            return render(request,'com-login.html',{'msg':'Incorrect Password'})
        except:
            msg = 'Account Not Registered' 
            return render(request,'com-login.html',{'msg':msg})
    return render(request,'com-login.html')

def com_index(request):
    com = Com.objects.get(email=request.session['email'])
    return render(request,'com-index.html',{'com':com})

def com_FIR(request):
    com = Com.objects.get(email=request.session['email'])
    FIRs=FIR.objects.all()
    return render(request,'com-FIR.html',{'com':com, 'FIRs':FIRs})

def com_view_FIR(request,pk):
    com = Com.objects.get(email=request.session['email'])
    fir=FIR.objects.get(id=pk)
    return render(request, 'com-view-FIR.html',{'com':com,'fir':fir})

def com_com(request):
    com = Com.objects.get(email=request.session['email'])
    data = Complaint.objects.all()
    return render(request,'com-com.html',{'com':com,'data':data })

def com_view_com(request,pk):
    com = Com.objects.get(email=request.session['email'])
    data = Complaint.objects.get(id=pk)
    return render(request,'com-view-com.html',{'com':com,'data':data })

def com_ins(request):
    com = Com.objects.get(email=request.session['email'])
    ins = Ins.objects.all()
    return render(request,'com-ins.html',{'com':com,'ins':ins})

def com_man_ins(request,pk):
    com = Com.objects.get(email=request.session['email'])
    ins = Ins.objects.get(id=pk)
    if request.method == 'POST':
        ins.fname = request.POST['fname']
        ins.lname = request.POST['lname']
        ins.user_id = request.POST['user_id']
        if 'pic' in request.FILES:
            ins.pic = request.FILES['pic']
        
        ins.save()
    return render(request, 'com-man-ins.html',{'com':com,'ins':ins})

def com_station(request):
    com = Com.objects.get(email=request.session['email'])
    stations= Station.objects.all()
    return render(request, 'com-station.html',{'com':com,'stations':stations})

def com_view_station(request,pk):
    com = Com.objects.get(email=request.session['email'])
    stations= Station.objects.get(id=pk)
    if request.method == 'POST':
        stations.station = request.POST['station']
        stations.address = request.POST['address']
        if 'img' in request.FILES:
            stations.img = request.FILES['img']
        
        stations.save()
        msg='Data Updated'
        return render(request, 'com-view-station.html',{'com':com,'stations':stations,'msg':msg})
    else:
        return render(request, 'com-view-station.html',{'com':com,'stations':stations})

def com_con(request):
    com = Com.objects.get(email=request.session['email'])
    con=Cons.objects.all()
    return render(request, 'com-con.html',{'com':com,'con':con})



