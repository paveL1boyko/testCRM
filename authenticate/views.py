from django.db.models import *
from django.db.models.functions import Concat
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from .forms import PersonForm
from .models import Person, Course, Address


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


def person_list(request):
    p = Address.objects.all()
    g = Person.objects.aggregate(c=Count('id'))
    Course.objects.filter(pk=1).update(title=Concat(F('title'), Value(' 1')))
    return render(request, 'authenticate/person_list.html', {'person_list': p})
