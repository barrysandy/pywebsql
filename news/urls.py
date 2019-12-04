from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('listArts/', views.listArts, name='listArts'),
    path('art/', views.art, name='art'),
    path('test/<int:html>', views.test, name='test'),

]
