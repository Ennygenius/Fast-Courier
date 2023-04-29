from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def index( request):
    if request.method == "POST":
        form =  LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        # messages.error(request, "Invalid Tracking Id")
        form = LoginForm()
    return render(request, 'index.html', {"form":form})
        



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url =  reverse_lazy('index')
    template_name = "signup.html"


# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             form = UserCreationForm()
#         return render(request, 'signup.html', {"form":form})

def about( request):
    return render (request, 'about.html')



def contact( request):
    return render (request, 'contact.html')


def service( request):
    return render (request, 'service.html')   


def price( request):
    return render (request, 'price.html') 

@login_required(login_url='/')
def home( request):
    return render (request, 'home.html')   

def logout_view(request):
    logout(request)
    return redirect('/')