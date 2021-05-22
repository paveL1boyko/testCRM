from django.urls import path
from django.views.generic import ListView

from authenticate.models import Person
from authenticate.views import PersonListView

urlpatterns = [
    path('person', ListView.as_view(model=Person, paginate_by=2), name='list_person'),
]
