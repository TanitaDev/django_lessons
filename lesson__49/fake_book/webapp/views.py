from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def second_page_view(request):
    return render(request, 'second_page.html')


def third_page_view(request):
    return render(request, 'third_page.html')
