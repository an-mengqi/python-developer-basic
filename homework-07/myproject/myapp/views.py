import time

from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from myapp.models import Person
from . import tasks
# Create your views here.


class PageTitleMixin:
    page_title = 'The Wall of Honor'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # print(f'{context=}')
        context['page_title'] = self.page_title

        return context


class PersonList(PageTitleMixin, ListView):
    page_title = 'People'
    model = Person
    paginate_by = 3


def send_mail(request):
    task_id = None

    print('task started', time.time())

    task = tasks.send_mail_task.delay('hello from Django', 'abcde')  # celery case
    # task = tasks.send_mail_task('hello from Django', 'abcde')  # sync case

    print('django works', time.time())

    try:
        task_id = task.id
        print('task_id', task_id)
    except Exception as e:
        pass

    context = {
        'task_id': task_id
    }
    return render(request, 'myapp/send_mail.html', context=context)


class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    success_url = '/'


class PersonDetail(PageTitleMixin, DetailView):
    model = Person
