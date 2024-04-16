from django.shortcuts import render
from myapp.models import Person
# Create your views here.


def index(request):
    people_qty = Person.objects.count()

    people = Person.objects.all()
    context = {
        'people': people,
        'people_qty': people_qty,
    }

    return render(request, "myapp/index.html", context=context)

