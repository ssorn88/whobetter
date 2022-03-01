from django.core import serializers
from django.shortcuts import render
from promiseapp.models import DepartCon, Depart, Candidate

# Create your views here.
from django.views.generic import ListView

from promiseapp.models import DepartCon


def home(request):
    return render(request, 'promiseapp/home.html')


class CandidateListView(ListView):
    model = DepartCon
    template_name = 'promiseapp/compare.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        departcons = DepartCon.objects.all()
        departs = Depart.objects.all()
        candies = Candidate.objects.all()

        departcon_json = serializers.serialize('json', departcons)
        depart_json = serializers.serialize('json', departs)
        candidate_json = serializers.serialize('json', candies)

        context = {
            "candidate_list" :  departcons,
            "departcon_json" : departcon_json,
            "depart_json": depart_json,
            "candidate_json": candidate_json
        }