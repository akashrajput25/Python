from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
#password for user akashrajput25 is akash250799

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request,'index.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        username = authenticate(username = username , password = password)
        if username is not None:
            login(request , username)
            return redirect('/')
    else:
        return render(request,'login.html')

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')