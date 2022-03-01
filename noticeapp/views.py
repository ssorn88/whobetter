
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView

from noticeapp.forms import NoticeCreationForm
from noticeapp.models import Notice


class NoticeCreateView(CreateView):
    model = Notice
    form_class = NoticeCreationForm
    template_name = 'noticeapp/create.html'

    def get_success_url(self):
        return reverse('promiseapp:main')


class NoticeListView(ListView):
    model = Notice
    context_object_name = 'notice_list'
    template_name = 'noticeapp/list.html'
    paginate_by = 25



