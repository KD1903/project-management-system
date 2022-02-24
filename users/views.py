from django.shortcuts import render, HttpResponse, redirect

import datetime as dt

import uuid
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from users.models import Member
from projects.models import Project

# Create your views here.
def user_login(request):
    
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_as = request.POST.get('account')

        user_obj=User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request,'User Not Found')
            return redirect('login')

        if login_as == "leader":
            profile_obj = Member.objects.filter(user = user_obj ).first()
            if profile_obj.role != 'leader':
                messages.success(request, 'you don\'t have leader access')
                return redirect('login')

        user=authenticate(username=username,password=password)
        if user is None:
            messages.success(request,'wrong credentials')
            return redirect('login')

        login(request, user)
        return redirect('dashboard/')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        register_as = request.POST.get('account')

        try:
            if username == None:
                messages.success(request, 'Username required')
                return redirect('/register')

            if email == None:
                messages.success(request, 'Username required')
                return redirect('/register')

            if User.objects.filter(username=username).first():
                messages.success(request, 'Username already registered')
                return redirect('/register')

            if User.objects.filter(email=email).first():
                messages.success(request, 'Email already registered')
                return redirect('/register')

            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()

            profile_obj = Member.objects.create(user=user_obj)

            if register_as == "leader":
                profile_obj.role = "leader"
                
            profile_obj.user_name = username
            profile_obj.save()

            return redirect('/login')

        except Exception as e:
            print(e)

    return render(request, 'register.html')

def logout_user(request):
    logout(request)
    return redirect('/login')

def dashboard(request):
    username = request.user
    user = Member.objects.get(user=username)

    projects = Project.objects.all()
    titles = []
    discription = []
    admin = []

    for i in projects:
        team = list(i.team.strip('[').strip(']').replace("'", "").split(', '))

        if user.user_name in team or user.user_name == i.admin:
            titles.append(i.title)
            discription.append(i.discription)
            admin.append(i.admin)


    context = {
        'username': username,
        'role': user.role,
        'data': list(zip(titles, discription, admin)),
    }

    return render(request, 'dashboard.html', context)