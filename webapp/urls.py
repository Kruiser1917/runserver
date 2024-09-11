from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),  # Маршрут для каталога
]

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('category/', views.category, name='category'),
    path('contacts/', views.contacts, name='contacts'),  # Маршрут для контактов
]

