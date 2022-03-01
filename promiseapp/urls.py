from django.urls import path


from promiseapp.views import home, CandidateListView

app_name = "promiseapp"

urlpatterns = [
    path('home/', home, name='home'),
    path('compare/', CandidateListView.as_view(), name='compare')
]