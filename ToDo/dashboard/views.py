from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import forms

# Create your views here.


def home(request):
    return render(request, 'home.html')
