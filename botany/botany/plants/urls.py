from django.contrib import admin
from django.urls import path
from plants import views

urlpatterns = [
path("", views.index, name='home'),

path("findaplant", views.find, name='find'),
path("addaplant", views.add, name='add'),
path("deleteaplant", views.delete, name='delete'),
path('confirm_delete/', views.confirm_delete, name='confirm_delete')
    
]
