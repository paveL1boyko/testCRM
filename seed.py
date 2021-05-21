import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testCRM.settings')
django.setup()

from django_seed import Seed

from authenticate.models import *

seeder = Seed.seeder()
COUNT_TABLE_ROW = 5
seeder.add_entity(Address, COUNT_TABLE_ROW)

random_MARKS = lambda x: random.choice(range(1, 11))

seeder.add_entity(Performance, COUNT_TABLE_ROW, dict(
    active=random_MARKS,
    mark_for_practice=random_MARKS,
    mark_for_theories=random_MARKS,
    visiting=lambda x: random.choice(range(3))
))

seeder.add_entity(Status, COUNT_TABLE_ROW, {
    'title': lambda x: random.choice(['teacher', 'student', 'manager']),
})

seeder.add_entity(Person, COUNT_TABLE_ROW, dict(
    phone='+375 26 555 44 44',
    # status={random.choice(range(COUNT_TABLE_ROW))},
    # courses={random.choice(range(COUNT_TABLE_ROW))}
))

seeder.add_entity(Course, COUNT_TABLE_ROW, {
    'title': lambda x: random.choice(['python', 'GO', 'JS', 'Sass']),
})

seeder.add_entity(CoursePerformance, COUNT_TABLE_ROW)
seeder.execute()
