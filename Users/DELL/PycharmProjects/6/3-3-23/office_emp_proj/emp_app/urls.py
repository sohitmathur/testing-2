"""office_emp_proj URL Configuration

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
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('all_emp', all_emp,name='all_emp'),
    path('add_emp', add_emp,name='add_emp'),
    path('remove_emp', remove_emp,name='remove_emp'),
    path('remove_emp/<int:emp_id>', remove_emp,name='remove_emp'),
    path('filter_emp', filter_emp,name='filter_emp'),
]
