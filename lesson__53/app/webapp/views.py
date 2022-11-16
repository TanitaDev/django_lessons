from django.http import HttpResponseRedirect

from webapp.models import Article

from django.shortcuts import render, get_object_or_404
from django.urls import reverse


def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def article_create_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'article_create.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('content')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, text=text, author=author)
        url = reverse('article_view', kwargs={'pk': article.pk})
        return HttpResponseRedirect(url)


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)
