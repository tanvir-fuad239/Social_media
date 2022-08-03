from django.urls import path
from App_Login import views

app_name = "App_Login"

urlpatterns = [
    
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login_user, name='login'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('edit-profile/', views.edit_user_profile, name='edit_user_profile'),
    path('public-user-profile/<str:username>/', views.public_user_profile, name='public_user_profile'),
    path('change-settings/', views.change_settings, name='change_settings'),
    path('password/', views.change_password, name='change_password'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('logout/', views.logout_user, name='logout'),
]
