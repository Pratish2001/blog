"""Blogsitepro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blogsiteapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.form,name="home"),
    path('show',views.show,name="show"),
    path('delete<int:id>',views.delete,name="delete"),
    path('update<int:id>',views.update,name="update"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('readmore<int:id>',views.readmore,name='readmore'),
    path('search',views.search,name='search'),
    path('edit<int:id>',views.edit,name="edit"),
    path('delete<int:id>',views.delete,name="delete"),
    path('profile',views.profile_func,name="profile"),
    path('editprofile<int:id>',views.editprofile,name="editprofile"),
    path('about',views.about_us,name='about')
       

]
