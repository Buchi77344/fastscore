from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('base', views.base, name='base'),
    path('post_de/<slug:slug>/',views.post_de, name='post_de')
]