from django.urls import path
from . import views

urlpatterns = [
    path('',views.currentUsers, name='user_list'),
    path('register/', views.registerClient, name='user_register'),
]
