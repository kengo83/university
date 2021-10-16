from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import CreateModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request,'signup.html',{'success':'ユーザー登録できました。'})
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザーは既に登録されています。'})
    return render(request,'signup.html')

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            return render(request,'login.html',{'error':'ログインできてません。'})
    return render(request,'login.html')

def menufunc(request):
    return render(request,'menu.html')

class Createfunc(CreateView):
    template_name = "create_class.html"
    model = CreateModel
    fields = ('class_name',)
    success_url = reverse_lazy('menu')
