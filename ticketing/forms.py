from django import forms

from ticketing.models import ShowTime, Cinema, Movie


class ShowTimeSearchForm(forms.ModelForm):
    movie_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    cinema_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    sale_open = forms.BooleanField(label='فقط سانس‌های قابل خرید', required=False)

    class Meta:
        model = ShowTime
        fields = ['movie_name', 'cinema_name', 'sale_open']


class MovieSearchForm(forms.ModelForm):
    movie_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Movie
        fields = ['movie_name']


class CinemaSearchForm(forms.ModelForm):
    cinema_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Cinema
        fields = ['cinema_name']
