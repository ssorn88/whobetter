from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


# Create your views here.
<<<<<<< HEAD
from django.urls import reverse
from django.utils.translation import template


def home(request):
    return render(request,'promiseapp/home.html')
=======
from django.views.generic import ListView

from promiseapp.models import DepartCon


def home(request):
    return render(request, 'promiseapp/home.html')


class CandidateListView(ListView):
    model = DepartCon
    context_object_name = 'candidate_list'
    template_name = 'promiseapp/compare.html'
>>>>>>> develop
