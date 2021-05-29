from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from .forms import PersonForm
from .models import Person


class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'

    # def get_template_names(self):
    #     return super().get_template_names()


class PersonListView(ListView):
    model = Person
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        data['form'] = PersonForm()
        return data


class PersonCreateView(CreateView):
    model = Person
    template_name = 'authenticate/person_list.html'
    form_class = PersonForm
    success_url = reverse_lazy('authenticate:person_list')


