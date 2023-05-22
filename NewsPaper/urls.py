"""NewsPaper URL Configuration

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
from django.urls import path, include
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contacts(request):
    return render(request, 'contacts.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('post.urls')),
    path('sign/', include('sign.urls')),
    path('', home, name='home'),
    path('templates/about.html', about, name='about'),
    path('templates/contacts.html', contacts, name='contacts'),
    path('accounts/', include('allauth.urls')),
]
