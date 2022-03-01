from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from promiseapp.models import DepartCon


def home(request):
    return render(request, 'promiseapp/home.html')


class CandidateListView(ListView):
    model = DepartCon
    context_object_name = 'candidate_list'
    template_name = 'promiseapp/compare.html'