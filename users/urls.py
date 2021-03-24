from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login_v, name='login'),
    path('logout/', views.logout_v, name='logout'),

]
