from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout

import datetime


# Create your views here.

def index(request):
    dt = datetime.datetime.now()
    aktuelle_kw = dt.isocalendar()[1]
    aktuelle_kw_string = "KW " + str(aktuelle_kw)

    return render(request, 'homepage/index.html', {'aktuelle_kw_string': aktuelle_kw_string})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'homepage/index.html')
            else:
                return render(request, 'homepage/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'homepage/login.html', {'error_message': 'Invalid login'})
    return render(request, 'homepage/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'homepage/login.html', context)

class UserFormView(View):
    form_class = UserForm
    template_name = 'homepage/registration_form.html'

    # fill user info
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    # submit user info to db
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})


