from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def home(request):
    return render(request,'home.html',{})


def login_cust(request):
    #records = Record.objects.all()
	# Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
		# Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('customer_login')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('customer_login')
    else:
        return render(request, 'cust_login.html', {})



def login_host(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
		# Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('host_login')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('host_login')
    else:
        return render(request, 'host_login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')
    




# Create your views here.
