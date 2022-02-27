from django.urls import path

from promiseapp.views import home

app_name = "promiseapp"

urlpatterns = [
    path('home/', home, name='promiseapp/home.html'),
]