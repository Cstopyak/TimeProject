from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib import *
from .models import *
import time
import calendar
import datetime
import bcrypt


def index(request):
    
    return render(request, "Login.html")

def registerPage(request):
    return render(request, 'register.html')

def registerProcess(request):
    print(request.POST)

    ValidationError = User.objects.regValidator(request.POST)
    print("Errors are below.")
    print(ValidationError)

    if len(ValidationError)> 0:
        for key, value in ValidationError.items():
            messages.error(request, value)
        return redirect("/registerPage")

    else: 
        hashedPassword = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt()).decode()
        newUser = User.objects.create(fname = request.POST['fname'], lname = request.POST['lname'], email = request.POST['email'], password = hashedPassword, Pto = 144)
        
    request.session['loginID'] = newUser.id 

    return redirect("/UserDashboard")

def UserDashboard(request):
    if 'loginID' not in request.session:
        messages.error(request, "Please log in.")
        return redirect("/")

    context ={
        'loginUser': User.objects.get (id= request.session['loginID']),
    }

    return render(request, 'UserDashboard.html', context)
def Calendar(request):
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 1, 4)
    delta = datetime.timedelta(days=1)

    while start_date <= end_date:
        print(start_date)
        start_date += delta

    return render(request, 'UserDashboard.html')


def MyBenefits(request):
    pto = User.objects.get(id=request.session['loginID'])
    context ={
        'loginUser': User.objects.get (id= request.session['loginID']),
        
    }


        
    return render(request, 'MyBenefits.html', context)

def BenefitsProcess(request):
    print(Request.POST)

def MyReports(request):

    context = {
        'scheduler': Scheduler.objects.all(),
    }
    return render(request, 'MyReports.html', context)

def SettingsPage(request):
    context ={
        'loginUser': User.objects.get (id= request.session['loginID'])
    }
    return render(request, 'Settings.html', context)

def Login(request):
    print(request.POST)
    ValidationError = User.objects.loginValidation(request.POST)
    print("Errors are below.")
    print(ValidationError)

    if len(ValidationError)> 0:
        for key, value in ValidationError.items():
            messages.error(request, value)
        return redirect("/")
    else:
        userswithSameEmail = User.objects.filter(email = request.POST['email'])
        request.session['loginID'] = userswithSameEmail[0].id

    return redirect("/UserDashboard")

def logout(request):
    request.session.clear()

    return redirect("/")

def clockIn(request):
    user =User.objects.get (id= request.session['loginID'])
    print(user.fname)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    Scheduler.objects.create(clock_in = current_time, employee= user)
    return redirect("/UserDashboard")

def clockOut(request):
    user =User.objects.get (id= request.session['loginID'])
    print(user.fname)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    Scheduler.objects.create(clock_out = current_time, employee= user)
    clockedin = Scheduler.clock_in
    clockedout = Scheduler.clock_out
    print(clockedin)
    print(clockedout)
    return redirect("/UserDashboard")

def requestTimeOff(request):
    user = User.objects.get(id=request.session['loginID'])
    pto_balance = user.Pto
    print(pto_balance)
    requestedPTO = request.POST["PtoRequested"]
    print(requestedPTO)
    requestedtimeoff = Requested.objects.create(RequestedTimeOff= requestedPTO, UserPTO= user)
    newPtoAmount = pto_balance - int(requestedPTO)
    print(newPtoAmount)
    user.Pto = newPtoAmount
    user.save()

    return redirect("/MyBenefits")