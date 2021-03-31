from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_v, name='login'),
    path('logout/', views.logout_v, name='logout'),
    path('profile/', views.profile_v, name='profile'),
    path('Edit_profile/', views.edit_profile, name='edit_profile'),
    path('make_user/', views.make_user, name='make_user'),
    path('payment/list/', views.payment_list, name='payment_list'),
    path('new/payment', views.new_payment, name='new_payment'),
    path('change_pass/', views.change_pass, name='change_pass'),
]
