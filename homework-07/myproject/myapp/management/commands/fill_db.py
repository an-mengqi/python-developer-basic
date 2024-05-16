from django.core.management.base import BaseCommand

from myapp.models import Person, PersonProfile, Position, Achievement


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        positions = Position.objects.all()

        # удаление данных
        positions.delete()

        # создание
        accountant_general = Position.objects.create(name='Director general')
        director_general = Position.objects.create(name='Accountant general')
        interpreter = Position.objects.create(name='Interpreter')

        director_v = Person.objects.create(
            name='Vasilii',
            position=director_general,
            age=50,
            # position_id=1,
        )

        accountant_n = Person.objects.create(
            name='Nataly',
            position=accountant_general,
            age=45,
        )

        interpreter_e = Person.objects.create(
            name='Elizabeth',
            position=interpreter,
            age=30,
        )

        best_worker_medal = Achievement.objects.create(name='"Worker of the year" medal')
        best_worker_medal.person.add(accountant_n)

        communication_diploma = Achievement.objects.create(name='"The best communication connect creator of a company" diploma')
        communication_diploma.person.add(interpreter_e)

        director_profile = PersonProfile.objects.create(about_person='Likes active sports while spending free time', person=director_v)

        self.stdout.write(
            self.style.SUCCESS('DB is ready')
        )
