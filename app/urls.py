from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('completed/<str:pk>/',completed,name='completed'),
    path('delete/<str:pk>/',delete,name='delete'),
    path('add/',Add,name='add'),
    path('edit/<str:pk>',Edit,name='edit'),
    path('login/',login_page,name='login'),
    path('logout/',LogOut,name='logout'),
    path('register/',register,name='register'),
]