from django.shortcuts import render ,redirect
from .forms  import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    user=request.user
    print(user.get_username())
    return render(request,'ev',{'name':user.get_username()})

def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user= authenticate(username=username,password=password)
        login(request,user)  
        print(type(user))

        return redirect('ev')
    return render(request,'login.html',{'form':form})

def register(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, 'lennon@thebeatles.com', password)
        login(request,user)
        
        print(dir(user))

        return redirect('ev')
    return render(request,'register.html',{'form':form})
