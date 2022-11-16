from django.http import HttpResponseRedirect

from webapp.forms import ArticleForm
from webapp.models import Article

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context


class ArticleView(TemplateView):
    template_name = 'article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=kwargs['pk'])
        return context


class ArticleCreate(TemplateView):
    template_name = 'article_create.html'

    def get_context_data(self, **kwargs):
        form = ArticleForm()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


class UpdateView(TemplateView):
    template_name = 'update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = ArticleForm(instance=context['article'])
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article.title = form.cleaned_data.pop('title')
            article.author = form.cleaned_data.pop('author')
            article.text = form.cleaned_data.pop('text')
            article.save()
            return redirect('article_view', pk=article.pk)


class DeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        return render(request, 'delete.html', context={'article': article})

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        article.delete()
        return redirect('index')
