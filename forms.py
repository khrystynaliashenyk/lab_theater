from django import forms
from theater_lab.models import Actor

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'date_of_birth']