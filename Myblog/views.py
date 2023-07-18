from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Article

def accueil(request):
    derniers_articles = Article.objects.order_by('-date_creation')[:4]
    context = {
        'derniers_articles': derniers_articles
    }
    return render(request, 'accueil.html', context)

def detail(request,id_article):
    article=Article.objects.get(id=id_article)
    return  render(request, 'detail.html',{"article":article})
