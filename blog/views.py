from django.shortcuts import render
from blog.models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all()  # 获取全部的Article对象
    article_num = len(articles)
    articles = articles[0:4]
    return render(request, 'home.html', {'articles': articles, 'article_num': article_num})


def detail(request, article_id):
    current_article = Article.objects.get(id=article_id)
    return render(request, 'article.html', {'current_article': current_article})


def about_me(request):
    return render(request, 'aboutMe.html')


def contact(request):
    return render(request, 'contact.html')


def pre(request):
    articles = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'pre.html', {'articles': articles})
