"""advtemplate URL Configuration

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
from car import views as v1
from home import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/',v1.car_info),
    path('',v2.index),
    path('petrol/',v1.petrol),
    path('diesel/',v1.diesel),
    path('cng/',v1.cng),
    path('electrical/',v1.electrical)
]
