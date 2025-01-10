from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login
 #password for test user- abd@1234
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        print("herere......")
        email=request.POST.get('email')
        password=request.POST.get('password')
        User = authenticate(email=email, password=password)
        if email is not None:
            login(request,User)
            return redirect("/")
        else:
            return render(request, 'login.html',{'error': 'Invalid login credentials'})
        
    return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    return redirect ("/login")   