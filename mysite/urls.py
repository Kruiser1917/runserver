from django.contrib import admin
from django.urls import path, re_path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Маршрут для главной страницы с именем 'index'
    path('catalog/', views.catalog, name='catalog'),
    path('category/', views.category, name='category'),
    path('contacts/', views.contacts_page, name='contacts'),
    re_path(r'^.*$', views.contacts_page),  # Обработка всех остальных запросов
]
