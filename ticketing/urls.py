from django.urls import path

from ticketing import views

app_name = 'ticketing'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('movie/list/', views.movie_list, name='movie_list'),
    path('cinema/list/', views.cinema_list, name='cinema_list'),
    path('showtime/list/', views.showtime_list, name='showtime_list'),
    path('movie/details/<int:movie_id>', views.movie_details, name='movie_details'),
    path('cinema/details/<int:cinema_id>', views.cinema_details, name='cinema_details'),
    path('tickets/list', views.ticket_list, name='ticket_list'),
    path('ticket/details/<int:ticket_id>', views.ticket_details, name='ticket_details'),
    path('ticket/buy/<int:showtime_id>', views.buy_ticket, name='buy_ticket'),
    path('about/', views.about, name='about'),
]
