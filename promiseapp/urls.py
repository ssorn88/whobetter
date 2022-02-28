from django.urls import path

from promiseapp.views import compare

app_name = "promiseapp"

urlpatterns = [
    path('compare/', compare, name='compare')
]