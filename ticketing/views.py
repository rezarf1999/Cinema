from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

import ticketing
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


@login_required
def buy_ticket(request, showtime_id):
    showtime = ShowTime.objects.get(pk=showtime_id)

    context = {
        'showtime': showtime,

    }
    if request.method == 'POST':
        try:
            seat_count = int(request.POST['seat_count'])
            assert showtime.status == showtime.sale_start, 'خرید بلیت برای این سانس امکانپذیر نمیباشد'
            assert showtime.free_seats >= seat_count, 'صندلی خالی به میزان انتخاب شده وجود ندارد'
            total_price = showtime.price * seat_count
            assert request.user.profile.buy(total_price), 'اعتبار حساب برای خرید کافی نمیباشد'
            showtime.reserve_seats(seat_count)
            ticket = Ticket.objects.create(showtime=showtime, customer=request.user.profile, seat_count=seat_count)
        except Exception as e:
            context['error'] = str(e)
        else:
            return HttpResponseRedirect(reverse('ticketing:ticket_details', kwargs={'ticket_id': ticket.id}))
    return render(request, 'ticketing/buy_ticket.html', context)


def home(request):
    return render(request, 'ticketing/home.html', {})
