from django import forms
import requests


response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
currencies = response.get('rates')
GEEKS_CHOICES = [(v, k) for k, v in currencies.items()]


class ConverterFrom(forms.Form):
    amount = forms.IntegerField(label='Amount', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    convert_from = forms.ChoiceField(choices=GEEKS_CHOICES, label='From', widget=forms.Select(attrs={'class': 'form-control'}))
    convert_to = forms.ChoiceField(choices=GEEKS_CHOICES, label='To', widget=forms.Select(attrs={'class': 'form-control'}))
