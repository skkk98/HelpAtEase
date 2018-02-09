from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Type
# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'

class Register(View):
    form_class = RegisterForm
    template_name = 'register.html'
    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            registeras = form.cleaned_data['RegisterAs']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            login(request, user)
            user_id = request.user
            reg = Type(user=user_id, RegisterAs=registeras)
            reg.save()
            logout(request)
            return HttpResponse('successfully registered')

        return render(request, self.template_name, {'form': form})

class Login(View):
    form_class = LoginForm
    template_name = 'login.html'
    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form =self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            registeras = form.cleaned_data['RegisterAs']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if Type.objects.filter(user=request.user, RegisterAs=registeras).exists():
                    return HttpResponseRedirect('/'+registeras.lower()+'/profile')
            else:
                return HttpResponse('<a href=""><strong>Click Here</strong></a> <a>to try again!</a>')
        return render(request, self.template_name, {'form': form})
