from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'home.html')

def loginattempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.error(request, "username Not Found")
            return redirect('login')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Your Passowrd Invailed")
            return redirect('logins')
        
        login(request, user)
        return redirect('home')   
    return render(request, 'login.html')

@csrf_exempt
def logoutattempt(request):
    if(request.user.is_authenticated is False):
        return redirect("logins")
    logout(request)
    return redirect('logins')

def registerattempt(request):
    if request.method == 'POST':
        first_name  = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        if User.objects.filter(username=username).first():
            messages.error(request, 'User Name Already Exists')
            return redirect('registers')
        
        if User.objects.filter(email=email).first():
            messages.error(request, 'Email Address already Exists')
            return redirect('registers')
        
        if Profile.objects.filter(mobile=mobile).first():
            messages.error(request, 'Email Address already Exists')
            return redirect('registers')
        
        user_obj = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        
        name = first_name + ' ' + last_name
        profile_obj = Profile.objects.create(user=user_obj, name=name, email=email, mobile=mobile)
        profile_obj.save()
        messages.success(request, 'Your Resgister Has been Successfully')
        return redirect('logins')
        
    return render(request, 'register.html')
        

def rental(request):
    if(request.user.is_authenticated is False):
        return redirect("logins")
    vr = Vehicle.objects.all()
    if request.method == 'POST':
        vehicle = request.POST.get('vehicle')
        rental_date = request.POST.get('rental_date')
        return_date = request.POST.get('return_date')
        mobile = request.POST.get('mobile')
        

        data = RentVehicle()
        data.username = request.user.first_name + ' ' + request.user.last_name
        data.useremail = request.user.email
        data.usermobile =mobile
        data.vehicle = vehicle
        data.rental_date = rental_date
        data.return_date = return_date
        data.save()
        
        
    return render(request, 'rental.html', {'vr':vr})

def customerlist(request):
    if(request.user.is_authenticated is False):
        return redirect("logins")
    customer = Profile.objects.all()
    return render(request, 'customerlist.html', {'customer':customer})

def rentallist(request):
    if(request.user.is_authenticated is False):
        return redirect("logins")
    vehicle = RentVehicle.objects.all()
    return render(request, 'rentallist.html', {'vehicle':vehicle})

def vehiclesavailable(request):
    if(request.user.is_authenticated is False):
        return redirect("logins")
    vc = Vehicle.objects.all()
    return render(request, 'availablevehicle.html', {'vc': vc})