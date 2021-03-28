from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_v, name='login'),
    path('logout/', views.logout_v, name='logout'),
    path('profile/', views.profile_v, name='profile'),
    # path('payment/list/', views.payment_list, name='payment_list'),
    # path('payment/create/', views.payment_create, name='payment_create'),
]
