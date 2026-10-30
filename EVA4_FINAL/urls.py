"""
URL configuration for EVA4_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.generic.base import TemplateView

from reservasAPP.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", TemplateView.as_view(template_name="landing.html"), name="landing"),
    path("index/", TemplateView.as_view(template_name="index.html"), name="home"),

    path('reservas/', reservasData, name='reservas'),
    path('registroReservas', registroReservas, name="registroReservas"),
    path('eliminarReservas/<int:id>', eliminarReservas, name="eliminarReservas"),
    path('editarReservas/<int:id>', editarReservas, name="editarReservas"),

    path('estados/', estadosData, name='estados'),
    path('registroEstados', registroEstados, name="registroEstados"),
    path('eliminarEstados/<int:id>', eliminarEstados, name="eliminarEstados"),
    path('editarEstados/<int:id>', editarEstados, name="editarEstados"),

    path('reservasAPI/', lista_reservas),
    path('reservasAPI/<int:pk>/', detalle_reservas),
]
