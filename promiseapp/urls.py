from django.urls import path, include


from promiseapp.views import CandidateListView, home

app_name = "promiseapp"

urlpatterns = [
    path('main/', home, name='main'),
    path('compare/', CandidateListView.as_view(), name='compare')
]