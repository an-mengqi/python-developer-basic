import time

from django.shortcuts import render
from myapp.models import Person
from . import tasks
# Create your views here.


def index(request):
    people_qty = Person.objects.count()

    people = Person.objects.all()
    context = {
        'people': people,
        'people_qty': people_qty,
    }

    return render(request, "myapp/index.html", context=context)


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
