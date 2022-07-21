import json

from django.shortcuts import render
import requests

from converter.forms import ConverterFrom


def converter_2(request):
    if request.method == 'POST':
        form = ConverterFrom(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        converted_amount = round((float(request.POST['convert_to']) / float(request.POST['convert_from'])) * float(request.POST['amount']), 2)
        context = {
            'form': form,
            'converted_amount': converted_amount,
        }
    else:
        form = ConverterFrom()
        context = {
            'form': form,
        }
    return render(request,'converter/index2.html', context)