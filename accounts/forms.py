from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from accounts.choices import gender_choice
from accounts.models import Profile, Payment


class UserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    password = None


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'gender', 'birthday', 'city', 'address', 'avatar']

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=gender_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'phone', 'gender', 'birthday', 'city', 'address']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'transaction_code']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'transaction_code': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ChangePassForm(PasswordChangeForm):
    old_password = forms.CharField(label='گذرواژه قدیمی', max_length=100,
                                   widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}))
    new_password1 = forms.CharField(label='گذرواژه جدید', max_length=100,
                                    widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='تایید گذرواژه جدید', max_length=100,
                                    widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}))

    class Meta(forms.Form):
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
