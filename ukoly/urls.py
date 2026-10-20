from django.urls import path
from . import views

urlpatterns = [
    path('', views.ukol_list, name='ukol_list'),
]