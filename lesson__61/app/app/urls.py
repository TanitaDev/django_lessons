from django.contrib import admin
from django.urls import path
from webapp.views import *
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>', ArticleView.as_view(), name='article_view'),
    path('articles/add', ArticleCreate.as_view(), name='article_add'),
    path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),

    path("accounts/", include('accounts.urls'))
]
