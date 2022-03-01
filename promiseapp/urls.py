from django.urls import path

from promiseapp.views import CandidateListView

app_name = "promiseapp"

urlpatterns = [
    path('compare/', CandidateListView.as_view(), name='compare')
]