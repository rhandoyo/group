from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from .models import Post, Usermasuk
# Create your views here.

def index(request):
    posts = Post.objects.all();
    usermasuks = Usermasuk.objects.all();
    
    context = {
        'title':'index',
        'posts':posts,
        'user_masuk':usermasuks
    }

    return render(request,'blog/index.html',context)

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password= password)

        if user:
            login(request,user)
            return redirect('/')
            
        else:
            messages.add_message(request,messages.INFO,'Username and password yang anda Masukkan salah' )
            return redirect('/login/')
    

    return render(request,'blog/login.html',context={})

@login_required
def logout_view(request):
    context = {
        'title':'Logout'
    }
    if request.method == 'POST':
        keluar = request.POST.get('keluar')
        if keluar:
            logout(request)
            return redirect('blog:login_view')
            
    return render(request,'blog/logout.html',context)

































