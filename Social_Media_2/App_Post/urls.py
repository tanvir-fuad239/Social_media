from django.urls import path
from App_Post import views

app_name = "App_Post"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('post-details/<pk>/', views.post_details, name='post_details'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/', views.unliked, name='unliked'),
    path('delete-post/<pk>/', views.delete_post, name='delete_post'),
]

