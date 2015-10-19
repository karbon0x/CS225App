from django.shortcuts import render
from django.views.generic import ListView, DetailView
from conflict.models import User_mod
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from conflict.forms import Signup,  sign_up_acc


def signup(request):
    if request.method == 'POST':
        user_form = Signup(data=request.POST)
        #profile_form = sign_up_acc(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

          #  profile = profile_form.save(commit=False)
           # profile.user = user

            #profile.save()
            return HttpResponseRedirect('/login/')
        else:
            error = "Please fill out all the fields"
            return render(request, 'error.html')
    else:
        user_form = Signup()
        #profile_form = sign_up_acc()
        return render(request, "sign.html", {'form': user_form}) #'form2': profile_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse('Your account is disabled. Please activate it')
        else:
            return HttpResponse("Login Failed, please check your username and password")
    else:
        return render(request, 'login.html')


@login_required
def index(request):
    if request.method == 'POST':
         user_form = sign_up_acc(data=request.POST)
         if user_form.is_valid():
            user1 = user_form.save(commit = False)
            user1.user = request.user
            user1.save()
            return HttpResponseRedirect('/success/')
    else:
        if request.user.is_authenticated():
            username = request.user.username
            ab = User_mod.objects.filter(user = request.user)
            if len(ab)>0:
                if ab[0].reason != 'Blank':
                    return HttpResponseRedirect('/success/')
            else:
                conflict_form = sign_up_acc()
                return render(request, 'index.html', {'obj': username,'for':conflict_form})

@login_required
def success(request):
    if request.user.is_authenticated():
        username = request.user.username
    return render(request, 'success.html', {'obj': username})
@login_required
def decision(request):
    if request.user.is_authenticated():
        username = request.user.username
    dec = User_mod.objects.filter(user = request.user)
    return render(request, 'decision.html', {'obj': username,'decision':dec[0]})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/login/')

# Create your views here.
