"""Ariadna URL Configuration

"""
from django.urls import path, include

urlpatterns = [
    path('', include('mainpage.urls')),
]
