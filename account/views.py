from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'blog/home.html')
def signup(request):
    if request.method=='POST':
        
        mail=request.POST.get('email','')
        name = request.POST.get('name', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        conf_pass = request.POST.get('confpass', '')
        

        userCheck=User.objects.filter(username=username)
        if userCheck:
            messages.error(request,'Username already taken')
            return  redirect('/')

        if password==conf_pass:
            user_obj=User.objects.create_user(first_name=name, password=password, email=mail, username=username)
            user_obj.save()
    return redirect('/')
def gotosignup(request):
    return render(request,'account/signup.html')
def user_login(request):
    if request.method=='POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')

        user = authenticate(username=user_name,password=user_password)
        #print(user)
        if user is not None:
            login(request, user)
            messages.success(request,'logged you in')
            return redirect('/blog')


        else:
            messages.error(request,'invalid username or password')
            return redirect('/')


def user_logout(request):
    logout(request)
    messages.success(request,'Logged out')
    return redirect('/')
