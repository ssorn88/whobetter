from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.translation import template


def home(request):
    return render(request,'promiseapp/home.html')