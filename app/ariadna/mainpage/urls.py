from django.urls import path

from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.index_page, name='home-page'),
    path('about', views.about_page, name='about-page'),
    path('knowledge', views.ArticleListView.as_view(), name='knowledge-page'),
    path('knowledge/<slug:slug>', views.ArticleDetailView.as_view(), name='article-detail'),
]
