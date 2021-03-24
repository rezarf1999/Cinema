from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_v(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'error': 'کاربری با مشخصات وارد شده در سیستم یافت نشد'
            }
            return render(request, 'users/login.html', context)

        else:
            login(request, user)
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))
        else:
            context = {}
            return render(request, 'users/login.html', context)


def logout_v(request):
    logout(request)

