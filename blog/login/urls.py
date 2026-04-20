from django.urls import path
from login import views

urlpatterns = [
    path('', views.users, name='index'),
    path('add_user/', views.add_user, name='add_user'),
    path('users/', views.users, name='users'),
]
