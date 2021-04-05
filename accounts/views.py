from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import ProfileForm, UserForm, AddUserForm, PaymentForm, ChangePassForm
from accounts.models import Profile, Payment


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
            login(request, user)
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))

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
    return render(request, 'accounts/edit_profile.html', context)


def make_user(request):
    form = AddUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.phone = form.cleaned_data.get('phone')
        user.profile.gender = form.cleaned_data.get('gender')
        user.profile.birthday = form.cleaned_data.get('birthday')
        user.profile.city = form.cleaned_data.get('city')
        user.profile.address = form.cleaned_data.get('address')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('accounts:profile')
    else:
        form = AddUserForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/make_user.html', context)


@login_required
def payment_list(request):
    payments = Payment.objects.filter(profile=request.user.profile).order_by('-transaction_time')
    context = {
        'payments': payments
    }
    return render(request, 'accounts/payment_list.html', context)


@login_required
def new_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.profile = request.user.profile
            payment.save()
            request.user.profile.increase_credit(payment.amount)
            return HttpResponseRedirect(reverse('accounts:payment_list'))
    else:
        form = PaymentForm
    context = {
        'form': form
    }
    return render(request, 'accounts/new_payment.html', context)


def change_pass(request):
    if request.method == 'POST':
        form = ChangePassForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePassForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
