from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('',Ask.as_view(),name='ask'),
    path('login/',Login.as_view(),name='login'),
    path('register/<role>',Register.as_view(),name='register'),
    path('logout/',Logout.as_view(),name='logout'),
    
]