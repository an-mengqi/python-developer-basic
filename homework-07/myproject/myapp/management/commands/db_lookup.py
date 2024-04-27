from django.core.management.base import BaseCommand

from myapp.models import Person, PersonProfile, Position, Achievement


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        pass
        # person = Person.objects.get(id=5)  # -> exc
        # person = Person.objects.filter(id=5).first()  # -> None
