from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


from django.views.generic import ListView

from promiseapp.models import DepartCon


def home(request):
    return render(request, 'promiseapp/home.html')


class CandidateListView(ListView):
    model = DepartCon
    context_object_name = 'candidate_list'
    template_name = 'promiseapp/compare.html'
