from authentication import views
from django.urls import path


urlpatterns=[
    path('/signup', views.RegisterAPIView.as_view(), name='signup'),
    path('/login', views.LoginAPIVIEW.as_view(), name='login'),
]