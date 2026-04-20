from django.urls import path
from login import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_user/', views.add_user, name='add_user'),
    path('users/', views.users, name='users'),
]
