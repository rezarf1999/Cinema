from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from ticketing.models import Movie, Cinema, ShowTime


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movie': movies
    }
    return render(request, 'ticketing/movie_list.html', context)


def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinema': cinemas
    }
    return render(request, 'ticketing/cinema_list.html', context)


def showtime_list(request):
    showtime = ShowTime.objects.all()
    context = {
        'showtime': showtime
    }
    return render(request, 'ticketing/showtime_list.html', context)


def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'ticketing/movie_details.html', context)


def cinema_details(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request, 'ticketing/cinema_details.html', context)


def showtime_list(request):
    showtime = ShowTime.objects.all()
    context = {
        'showtime': showtime
    }
    return render(request, 'ticketing/showtime_list.html', context)


def cin(request):
    context = {

    }
    return render(request, 'ticketing/test.html', context)


def login(request):
    context = {

    }
    return render(request, 'ticketing/login.html', context)
