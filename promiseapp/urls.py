from django.urls import path

<<<<<<< HEAD

from promiseapp.views import home, CandidateListView
=======
from promiseapp.views import CandidateListView
>>>>>>> develop

app_name = "promiseapp"

urlpatterns = [
<<<<<<< HEAD
    path('home/', home, name='home'),
=======
>>>>>>> develop
    path('compare/', CandidateListView.as_view(), name='compare')
]