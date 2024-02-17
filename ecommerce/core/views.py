from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from item.models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *

# Create your views here.
def Welcome(request):
    return render(request,'page/welcome.html',{'list':list})

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    return render(request,'page/index.html',{'items':items,'categories':categories})
def sign_up(request):
    form = usercreation()
    if request.method == 'POST':
        form = usercreation(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('/')
    else:
        form = usercreation()
    return render(request,'page/sign_up.html',{'form':form})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect('/')
        else:
            form = authentication()
            messages.info(request,'Username or password invalid pls1 try again ')
    else:
        form = authentication()
    return render(request,'page/login.html',{'form':form})
@login_required
def pass_change(request):
    if request.method == 'POST':
        form= PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('/')
    else :
        form = PasswordChangeForm(request.user)
    
    return render(request,'page/pass_change.html',{'form':form})
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

