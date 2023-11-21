from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('logout/', views.user_logout, name='logout')
]