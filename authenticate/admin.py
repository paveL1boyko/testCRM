from django.contrib import admin
from .models import Person, Address, Status, Course, Performance, CoursePerformance
# Register your models here.
admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Status)
admin.site.register(Course)
admin.site.register(Performance)


admin.site.register(CoursePerformance)