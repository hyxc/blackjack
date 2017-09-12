# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User
from .decorators import login_required
import hashlib

# Create your views here.
def login(request):
    if request.method == 'POST':
        uspa = UserForm(request.POST)
        if uspa.is_valid():
            username = uspa.cleaned_data['username']
            password = uspa.cleaned_data['password']
            passwdhash = hashlib.sha256(password+username+'ylhb').hexdigest()
            user = User.objects.filter(username__exact = username,password__exact = passwdhash)
            if user:
                request.session['username'] = username
                return render(request, 'accounts/dashboard.html')
            else:
                return render(request, 'accounts/login.html')
        else:
            return render(request, 'accounts/login.html')
    else:
        uspa = UserForm()
    return render(request, 'accounts/login.html')

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect('/accounts/login/')