from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def home(req):
    return render(req, "/aut/home.html")


def registration(req):
    if req.method == "POST":
        fname = req.POST.get("fname")
        lname = req.POST.get("lname")
        username = req.POST.get("username")
        email = req.POST.get("email")
        password1 = req.POST.get("password1")
        password2 = req.POST.get("password2")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(req, "username taken")
                return redirect("aut:registration")
            elif User.objects.filter(email == email).exists():
                messages.info(req, "email teken")
                return redirect("aut:registration")
            else:
                user = User.objects.create_user(
                    fname=fname,
                    lname=lname,
                    username=username,
                    email=email,
                    password=password1,
                )
                user.save()
                return redirect("aut:login")
        else:
            return redirect("aut:registration")
        return redirect("/")
    else:
        render(req, "aut/regitration.html")


def login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")

        user = auth.authentication(username=username, password=password)

        if user is not None:
            auth.login(req, user)
            return redirect("/")
        else:
            messages.info("credential is invalid")
            return redirect("aut:login")
    else:
        return render(req, "aut/login.html")


def logout(req):
    auth.logout(req)
    return redirect("/")
