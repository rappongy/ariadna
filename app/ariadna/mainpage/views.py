from collections import namedtuple

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article

def index_page(request):
    return render(request, 'mainpage/index.html')


def about_page(request):
    SliderImage = namedtuple('SliderImage', 'image caption year')

    slider = [
        SliderImage('mainpage/images/about/1.png', 'Выезд на тутальские скалы', 2019),
        SliderImage('mainpage/images/about/2.png', 'Олег пытается развязать узел', 2019),
        SliderImage('mainpage/images/about/3.png', 'Новички', 2019),
        SliderImage('mainpage/images/about/4.png', 'Тактовские спасы', 2018),
        SliderImage('mainpage/images/about/5.png', 'Этап бивуак на спасах', 2018),
        SliderImage('mainpage/images/about/6.png', 'Хэллоуин', 2018),
        SliderImage('mainpage/images/about/7.png', 'Тумба-юмба', 2018),
        SliderImage('mainpage/images/about/8.png', 'Тренировка на буревестнике', 2017),
        SliderImage('mainpage/images/about/9.png', 'Вязка жестких носилок', 2017),
        SliderImage('mainpage/images/about/10.png', 'Сосулька', 2013),
    ]

    Member = namedtuple('Member', 'name image caption')

    members_president = Member('Александра Диденко', 'mainpage/images/about/Аля.png', 'президент')
    members_other = [
        Member('Анастасия Черноштан', 'mainpage/images/about/Настя.png', 'казначей'),
        Member('Алексей Климов', 'mainpage/images/about/Климов.png', 'главный по снаряге'),
        Member('Алексей Таран', 'mainpage/images/about/Таран.png', 'тренер'),
        Member('Эмиль Мирмаметов', 'mainpage/images/about/Эмиль.png', 'администратор сайта, группы'),
    ]

    return render(request, 'mainpage/about.html', {
        'slider_images': slider,
        'members_president': members_president,
        'members_other': members_other,
    })


# def knowledge_page(request):
#     return render(request, 'mainpage/knowledge.html')


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article
