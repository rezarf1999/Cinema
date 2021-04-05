from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from ticketing.forms import ShowTimeSearchForm, MovieSearchForm, CinemaSearchForm
from ticketing.models import Movie, Cinema, ShowTime, Ticket, News


def movie_list(request):
    movie = Movie.objects.all()
    form = MovieSearchForm(request.GET)
    if form.is_valid():
        movie = movie.filter(name__contains=form.cleaned_data['movie_name'])
    context = {
        'movie': movie,
        'form': form
    }
    return render(request, 'ticketing/movie_list.html', context)


def cinema_list(request):
    cinema = Cinema.objects.all()
    form = CinemaSearchForm(request.GET)
    if form.is_valid():
        cinema = cinema.filter(name__contains=form.cleaned_data['cinema_name'])
    cinema = cinema.order_by('name')
    context = {
        'cinema': cinema,
        'form': form
    }
    return render(request, 'ticketing/cinema_list.html', context)


def showtime_list(request):
    showtime = ShowTime.objects.all()
    form = ShowTimeSearchForm(request.GET)
    if form.is_valid():
        showtime = showtime.filter(movie__name__contains=form.cleaned_data['movie_name'])
        if form.cleaned_data['sale_open']:
            showtime = showtime.filter(status=ShowTime.sale_start)
        if form.cleaned_data['cinema_name'] is not None:
            showtime = showtime.filter(cinema__name__contains=form.cleaned_data['cinema_name'])
    showtime = showtime.order_by('start_time')
    context = {
        'showtime': showtime,
        'form': form
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
            person_count = int(request.POST['person_count'])
            assert showtime.status == showtime.sale_start, 'خرید بلیت برای این سانس امکانپذیر نمیباشد'
            assert showtime.free_seats >= person_count, 'صندلی خالی به میزان انتخاب شده وجود ندارد'
            total_price = showtime.price * person_count
            assert request.user.profile.buy(total_price), 'اعتبار حساب برای خرید کافی نمیباشد'
            showtime.reserve_seats(person_count)
            ticket = Ticket.objects.create(customer=request.user.profile, showtime=showtime, person_count=person_count)
        except Exception as e:
            context['error'] = str(e)
        else:
            return HttpResponseRedirect(reverse('ticketing:ticket_details', kwargs={'ticket_id': ticket.id}))
    return render(request, 'ticketing/buy_ticket.html', context)


def home(request):
    movie = Movie.objects.all()[:2]
    news = News.objects.all()[:3]
    context = {
        'movie': movie,
        'news': news
    }
    return render(request, 'ticketing/home.html', context)


def about(request):
    return render(request, 'ticketing/about.html', {})
