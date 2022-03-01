from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'promiseapp/home.html')


def compare(request):
    return render(request, 'promiseapp/compare.html')
