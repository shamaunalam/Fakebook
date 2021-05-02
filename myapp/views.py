from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from .models import User_Profile

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,'index.html')






@login_required(login_url='index')
def home(request):

    user = request.user

    name = user.username.capitalize()

    pro = User_Profile.objects.get(user=user)

    context = {'name':name,'pro':pro}
    return render(request,'home.html',context)


@login_required(login_url='index')
def profile(request):
    user = request.user

    name = user.username.capitalize()

    pro = User_Profile.objects.get(user=user)

    context = {'name':name,'pro':pro}
    return render(request,'profile.html',context)

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:

            u = User(username=username)
            u.set_password(password1)
            u.save()
            return redirect('index')

        else:
            return redirect('index')
    else:
        return redirect('index')


def Login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            
            login(request,user)
            return redirect('home')
        else:
            return redirect('index')
    else:
        return redirect('index')

def Logout(request):

    logout(request)

    return redirect('index')

def update(request):

    if request.method=='POST':

        status = request.POST['status']
        location = request.POST['location']

        pro = User_Profile.objects.get(user=request.user)
        pro.status = status
        pro.location = location
        pro.save()

        return redirect('profile')
    else:
        return redirect('profile')