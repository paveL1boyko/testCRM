from django.urls import path
from django.views.generic import ListView

from authenticate.models import Person
from authenticate.views import PersonCreateView, PersonListView, person_list

app_name = 'authenticate'
urlpatterns = [
    path('person/', PersonListView.as_view(), name='person_list'),
    path('create/', PersonCreateView.as_view(), name='create'),
    path('1/', person_list),
]
