from django.db.models import Q
from django.utils.http import urlencode
from django.urls import reverse, reverse_lazy

from webapp.forms import ArticleForm, SearchForm
from webapp.models import Article

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'articles'
    model = Article
    ordering = 'created_at'
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().order_by("-title")
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(author__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset


class ArticleView(DetailView):
    template_name = 'article_view.html'
    model = Article
    pk_url_kwarg = 'pk'


class ArticleCreate(LoginRequiredMixin, CreateView):
    template_name = 'article_create.html'
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.pk})


class ArticleUpdate(UpdateView):
    template_name = 'update.html'
    model = Article
    form_class = ArticleForm
    context_object_name = 'article'

    def get_success_url(self):
        return reverse('article_view', kwargs={'pk': self.object.pk})


class ArticleDelete(DeleteView):
    template_name = 'delete.html'
    model = Article
    context_object_name = 'article'
    success_url = reverse_lazy('index')

