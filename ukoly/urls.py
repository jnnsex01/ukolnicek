from django.urls import path
from . import views

urlpatterns = [
    path('', views.ukol_list, name='ukol_list'),
    path('ukol/<int:pk>/', views.ukol_detail, name='ukol_detail'),
]