from django.views.generic import ListView

from authenticate.models import Person


class PersonListView(ListView):
    model = Person
    paginate_by = 2
