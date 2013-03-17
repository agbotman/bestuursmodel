from .models import *
from django.forms import ModelForm

class FunctieEisForm(ModelForm):
    class Meta:
        model = FunctieEis
