from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_v, name='login'),
    path('logout/', views.logout_v, name='logout'),
    path('profile/', views.profile_v, name='profile'),

]
