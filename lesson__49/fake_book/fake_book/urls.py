from django.contrib import admin
from django.urls import path
from webapp import views as webapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webapp_views.index_view),
    path('second_page/', webapp_views.second_page_view),
    path('second_page/third_page/', webapp_views.third_page_view)
]
