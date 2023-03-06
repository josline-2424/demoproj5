from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Store


# Create your views here.
def index(request):
    store = Store.objects.all()
    context = {'storelist': store}
    return render(request, 'index.html', context)

def demo(request):
    return render(request, 'index.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = auth.authenticate(username=username, password=pwd)
        if user is not None:
            auth.login(request, user)
            return render(request, 'form.html')
        else:
            messages.info(request, "Invalid credentials. Check again or register.")
            return render(request, 'login.html')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        if pwd == cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken. Try another name.")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=pwd)
                user.save()
                return render(request, 'login.html')
        else:
            messages.info(request, "Passwords do not match. Re-enter password")
            return render(request, 'register.html')
        return redirect('/')
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def formnew(request):
        store = Store.objects.all()
        context = {'storelist': store}
        return render(request, 'form.html', context)

def formreq(request):
    store = Store.objects.all()
    context = {'storelist': store}
    return render(request, 'index.html', context)
