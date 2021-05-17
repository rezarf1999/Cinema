from django.contrib import admin

from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_filter = ['director', 'year']
    search_fields = ['name', 'director']
    list_display = ['name', 'director', 'year']


admin.site.register(Movie, MovieAdmin)


class CinemaAdmin(admin.ModelAdmin):
    list_filter = ['name', 'capacity', 'city']
    search_fields = ['name', 'city']
    list_display = ['name', 'capacity', 'city']


admin.site.register(Cinema, CinemaAdmin)


class ShowTimeAdmin(admin.ModelAdmin):
    list_filter = ['movie', 'cinema', 'price', 'start_time']
    search_fields = ['movie', 'cinema', 'price', 'start_time']
    list_display = ['movie', 'cinema', 'price', 'start_time']


admin.site.register(ShowTime, ShowTimeAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_filter = ['showtime', 'buy_time', 'person_count']
    search_fields = ['customer']
    list_display = ['customer', 'showtime', 'buy_time']


admin.site.register(Ticket, TicketAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_filter = ['subject', 'time']
    search_fields = ['title']
    list_display = ['title', 'subject', 'time']


admin.site.register(News, NewsAdmin)
