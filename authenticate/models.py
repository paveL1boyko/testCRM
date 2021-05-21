from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

MARKS = list(enumerate(range(1, 11)))


class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    flat = models.CharField(max_length=100)
    post_office = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.country} {self.city}'


class Performance(models.Model):
    active = models.PositiveIntegerField(choices=MARKS)
    mark_for_practice = models.PositiveIntegerField(choices=MARKS)
    mark_for_theories = models.PositiveIntegerField(choices=MARKS)
    visits = [(0, 'exited'), (1, 'offline'), (2, 'online')]
    visiting = models.PositiveIntegerField(choices=visits)
    # performance = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.visits[self.visiting][1]}'


class Status(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    hours = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ManyToManyField('Person',
                                     limit_choices_to=models.Q(status__title='teacher'))

    def __str__(self):
        return self.title


class CoursePerformance(models.Model):
    performance = models.ForeignKey('Performance', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course}:{self.person}'


class Person(AbstractUser):
    # name = models.CharField(max_length=100)
    # surname = models.CharField(max_length=100)
    # username = models.CharField

    # email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    courses = models.ManyToManyField('Course', through_fields=('person', 'course'),
                                     through='CoursePerformance')
    status = models.ManyToManyField('Status')
    # date_created = models.DateTimeField(auto_created=True)
    changed = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d')


    def __str__(self):
        return f'{self.username}'


