import profile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from ticketing.models import Movie, Cinema, ShowTime, Ticket


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movie': movies,
    }
    return render(request, 'ticketing/movie_list.html', context)


def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinema': cinemas
    }
    return render(request, 'ticketing/cinema_list.html', context)


@login_required
def showtime_list(request):
    showtime = ShowTime.objects.all().order_by('start_time')
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


@login_required
def ticket_list(request):
    ticket = Ticket.objects.filter(customer=request.user.profile).order_by('-buy_time')
    context = {
        'ticket': ticket
    }

    return render(request, 'ticketing/ticket_list.html', context)


@login_required
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    context = {
        'ticket': ticket
    }
    return render(request, 'ticketing/ticket_details.html', context)


def test(request):
    return render(request, 'ticketing/test.html', {})
