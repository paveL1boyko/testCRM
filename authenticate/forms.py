from django import forms

from authenticate.models import Person


class PersonForm(forms.ModelForm):
    def save(self, commit=True):
        inst = super().save(commit=False)
        inst.set_password(self.cleaned_data['password'])
        inst.save()
        return inst

    class Meta:
        model = Person
        fields = ['username', 'email', 'password']
