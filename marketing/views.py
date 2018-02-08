from django.shortcuts import render
from django.views.generic import TemplateView,View
from .forms import RegisterForm
from django.http import HttpResponse
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
