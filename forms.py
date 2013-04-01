from .models import *
from django.forms import ModelForm

class FunctieForm(ModelForm):
    class Meta:
        model = Functie
        exclude = ('afdelingen',)
