from django.shortcuts import render

from news.models import News, Category
from django.views.generic import ListView


def news_page(request):
    news = News.objects.all()
    categories = Category.objects.all()
    return render(request, 'news/news.html', {'news': news, 'category': categories})


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news,'categories': categories, 'category': category})
