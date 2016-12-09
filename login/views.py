from django.http import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

def login_user(request):
    logout(request)
    username = password = server = ''
    if request.POST:
        webmail = request.POST['webmail']
        password = request.POST['password']
        server = request.POST['server']
        user = authenticate(webmail=webmail, password=password, server=server)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/login/home/')
    return render(request, 'login.html', {})

@login_required(login_url="/login/")
def home(request):
    return render(request, "home.html", {})

