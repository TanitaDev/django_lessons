from django.conf import settings
from django.conf.urls.static import static
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
    path('article/<int:pk>/to-favourite/', FavouriteView.as_view(), name='to_favourite'),

    path("accounts/", include('accounts.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
