from django.contrib import admin
from django.urls import path
from hoarding_app.views import *
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from hoarding_base import settings

urlpatterns = [path('signup/', SignUpView.as_view(), name='signup'),
               path('login/', AdminLogin.as_view(), name='login'),
               path('', HomeView.as_view(), name='home')]