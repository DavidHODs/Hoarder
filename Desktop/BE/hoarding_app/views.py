from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import *
from django.urls import reverse_lazy, reverse
from .forms import *
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib.auth.views import LoginView
# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class AdminLogin(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')


class HomeView(ListView):
    model = Post
    template_name = 'home.html'