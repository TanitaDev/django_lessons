from django.contrib import admin
from django.urls import path
from webapp.views import index_view, article_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index_view),
    path('', article_create_view)
]
