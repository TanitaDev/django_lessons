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


# def article_create_view(request, *args, **kwargs):
#     if request.method == 'GET':
#         form = ArticleForm()
#         return render(request, 'article_create.html', context={'form': form})
#     elif request.method == 'POST':
#         form = ArticleForm(data=request.POST)
#         if form.is_valid():
#             article = Article.objects.create(
#                 title=form.cleaned_data['title'],
#                 author=form.cleaned_data['author'],
#                 text=form.cleaned_data['text']
#             )
#             return redirect('article_view', pk=article.pk)
#         else:
#             return render(request, 'article_create.html', context={'form': form})

def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request, 'article_create.html', {'form': form})


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
            article = form.save()
            article.save()
            return redirect('article_view', pk=article.pk)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class DeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        return render(request, 'delete.html', context={'article': article})

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        article.delete()
        return redirect('index')
