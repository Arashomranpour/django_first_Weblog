import re
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from account.models import Profile  # <-- import your Profile model
from .forms import edituserform
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def mylogin(request):
    if request.user.is_authenticated:    
        return redirect("home_app:home")
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home_app:home")

    return render(request, "account/login.html",{})

def mylogout(request):
    logout(request)
    print(f"{request.user} is now logged out")
    return redirect("home_app:home")

def myregister(request):
    context = {"errors": []}
    if request.user.is_authenticated:
        return redirect("home_app:home")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        nationalcode = request.POST.get("nationalcode") or None
        image = request.FILES.get("image")

        # Validation
        if password != password2:
            context["errors"].append("Passwords do not match.")
            return render(request, "account/register.html", context)

        if User.objects.filter(username=username).exists():
            context["errors"].append("Username already exists.")
            return render(request, "account/register.html", context)

        if User.objects.filter(email=email).exists():
            context["errors"].append("Email already registered.")
            return render(request, "account/register.html", context)

        # ✅ Create user properly (hashed password)
        user = User.objects.create_user(username=username, email=email, password=password)

        # ✅ Create profile
        Profile.objects.create(user=user, nationalcode=nationalcode, image=image)

        # ✅ Authenticate and login
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home_app:home")

        context["errors"].append("Could not log you in automatically. Please log in manually.")
        return render(request, "account/register.html", context)

    return render(request, "account/register.html", context)



def edit_user(request):
    user=request.user
    form=edituserform(instance=user)
    if request.method=="POST":
        form=edituserform(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            # return redirect("home_app:home")


    return render(request,"account/editprofile.html",{"form":form})

