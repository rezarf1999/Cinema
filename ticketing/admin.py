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

admin.site.register(Ticket)
