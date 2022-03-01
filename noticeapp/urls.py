from django.urls import path

from noticeapp.views import NoticeCreateView

app_name = 'noticeapp'

urlpatterns = [
    path('create/', NoticeCreateView.as_view(), name = 'create'),
]