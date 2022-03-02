from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from promiseapp.views import CandidateListView, home

app_name = "promiseapp"

urlpatterns = [
    path('main/', home, name='main'),
    path('compare/', CandidateListView.as_view(), name='compare')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
