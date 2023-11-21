from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hotel/<slug:hotel_id>', views.hotel_details, name='hotel_details'),
    path('search/', views.search, name='search'),
    path('review/<int:hotel_id>/', views.submit_review, name='review'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),

]