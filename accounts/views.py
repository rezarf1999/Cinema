from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accounts.forms import ProfileForm, UserForm, AddUserForm
from accounts.models import Profile


def login_v(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'error': 'کاربری با مشخصات وارد شده در سیستم یافت نشد'
            }
            return render(request, 'accounts/login.html', context)

        else:
            if request.user.profile.id:
                login(request, user)
                return HttpResponseRedirect(reverse('ticketing:showtime_list'))
            else:
                context={
                    'error': 'برای استفاده از حسابتان باید یک پروفایل بسازید'
                }
                return HttpResponseRedirect(reverse('accounts:make_profile'))

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))
        else:
            context = {}
            return render(request, 'accounts/login.html', context)


def logout_v(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))


@login_required
def profile_v(request):
    profiles = Profile.objects.filter(user=request.user)
    context = {
        'profile': profiles
    }
    return render(request, 'accounts/profile.html', context)


# @login_required
# def payment_list(request):
#     payments = Payment.objects.filter(profile=request.user.profile).order_by('-transaction_time')
#     context = {
#         'payments': payments
#     }
#     return render(request, 'accounts/payment_list.html', context)
#
#
# @login_required
# def payment_create(request):
#     if request.method == 'POST':
#         payment_form = PaymentForm(request.POST)
#         if payment_form.is_valid():
#             payment = payment_form.save(commit=False)
#             payment.profile = request.user.profile
#             payment.save()
#             request.user.profile.deposit(payment.amount)
#             return HttpResponseRedirect(reverse('accounts:payment_list'))
#     else:
#         payment_form = PaymentForm()
#     context = {
#         'payment_form': payment_form
#     }
#     return render(request, 'accounts/payment_create.html', context)
#
#
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, files=request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/edit_account.html', context)


def make_user(request):
    if request.method == 'POST':
        add_user = AddUserForm(request.POST)
        if add_user.is_valid():
            add_user.save()
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        add_user = AddUserForm()
        context = {
            'add_user': add_user,
        }
        return render(request, 'accounts/make_user.html', context)


@login_required()
def make_profile(request):
    if request.method == 'POST':
        add_profile = ProfileForm(request.POST)
        if add_profile.is_valid():
            add_profile.save()
            return HttpResponseRedirect(reverse('accounts:make_profile'))
    else:
        add_profile = ProfileForm()
        context = {
            'add_profile': add_profile,
        }
        return render(request, 'accounts/make_profile.html', context)
