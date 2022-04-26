from django.shortcuts import render,redirect
from . models import *

# Create your views here.

def ins_login(request):
    if request.method == 'POST':
        try:
            ins = Ins.objects.get(email=request.POST['email'])
            if request.POST['password'] == ins.password:
                request.session['email'] = request.POST['email']
                return redirect('ins-index')
            return render(request,'ins-login.html',{'msg':'Incorrect Password'})
        except:
            msg = 'Account not registered' 
            return render(request,'ins-login.html',{'msg':msg})
    return render(request,'ins-login.html')

def ins_index(request):
    ins = Ins.objects.get(email=request.session['email'])
    return render(request,'ins-index.html',{'ins':ins})

def ins_view_FIR(request):
    ins = Ins.objects.get(email=request.session['email'])
    FIRs= FIR.objects.all()
    return render(request,'ins-view-FIR.html',{'ins':ins,'FIRs':FIRs})

def ins_view_one_FIR(request,pk):
    ins = Ins.objects.get(email=request.session['email'])
    fir=FIR.objects.get(id=pk)
    return render(request, 'ins-view-one-FIR.html',{'ins':ins,'fir':fir})

def ins_view_com(request):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.all()
    return render(request,'ins-view-com.html',{'ins':ins,'com':com})

def ins_view_one_com(request,pk):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.get(id=pk)
    return render(request, 'ins-view-one-com.html',{'ins':ins,'com':com})

def ins_manage_com(request):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.all()
    return render(request,'ins-manage-com.html',{'ins':ins,'com':com})

def ins_disable(request,pk):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.get(id=pk)
    com.status = False
    com.save()
    return redirect('ins-manage-com')

def ins_enable(request,pk):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.get(id=pk)
    com.status = True
    com.save()
    return redirect('ins-manage-com')

def ins_manage_view(request,pk):
    ins = Ins.objects.get(email=request.session['email'])
    com=Complaint.objects.get(id=pk)
    return render(request, 'ins-manage-view.html',{'ins':ins,'com':com})