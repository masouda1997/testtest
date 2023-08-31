from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(req):
    return render(req, "aut/home.html")


def registration_user(req):
    if req.method == "POST":
        fname = req.POST.get("fname")
        lname = req.POST.get("lname")
        username = req.POST.get("username")
        email = req.POST.get("email")
        password1 = req.POST.get("password1")
        password2 = req.POST.get("password2")
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(req, "username taken")
                return redirect("aut:registration")
            elif User.objects.filter(email = email).exists():
                messages.info(req, "email taken")
                return redirect("aut:registration")
            else:
                print("🔴🔴")
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name = fname,
                    last_name = lname,
                )
                # user.fname=fname
                user.lname=lname
                user.save()
                print("🟢")
                return redirect("aut:login")
        else:
            print("1️⃣")
            return redirect("aut:registration")
    print("2️⃣")
    return render(req, "aut/registration.html")


def login_user(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        print(username,password)
        user = authenticate(req ,username=username, password=password)
        print(user)
        if user is not None:
            login(req, user)
            return redirect("http://127.0.0.1:8000/app/")
        else:
            print("1️⃣")
            messages.error(req , "credential is invalid")
            return redirect("aut:login")
    print("2️⃣")
    return render(req, "aut/login.html")
            

def logout_user(req):
    logout(req)
    return redirect("/")
