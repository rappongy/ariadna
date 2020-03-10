from django.urls import path

from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.index_page, name='home-page'),
    path('about', views.about_page, name='about-page'),
]
