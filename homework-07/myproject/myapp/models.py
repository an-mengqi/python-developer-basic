from django.db import models

# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.PositiveIntegerField(null=True)
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name='people',
        null=True
    )   # position_id

    def __str__(self):
        return self.name


class PersonProfile(models.Model):
    about_person = models.TextField()
    person = models.OneToOneField(
        Person,
        primary_key=True,
        on_delete=models.CASCADE,
    )   # person_id


class Achievement(models.Model):
    name = models.CharField(max_length=50)
    person = models.ManyToManyField(Person)

    def __str__(self):
        return self.name
