from home import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
]