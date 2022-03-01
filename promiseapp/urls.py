from django.urls import path
<<<<<<< HEAD

from promiseapp.views import home

app_name = "promiseapp"

urlpatterns = [
    path('home/', home, name='home'),
=======

from promiseapp.views import compare

app_name = "promiseapp"
>>>>>>> develop

urlpatterns = [
    path('compare/', compare, name='compare')
]