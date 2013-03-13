from django.contrib import admin
from .models import *
from django.forms import Textarea, ModelForm, ModelMultipleChoiceField

class AfdelingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }

class FunctieEisInline(admin.TabularInline):
    model = FunctieEis.functies.through


class FunctieAdmin(admin.ModelAdmin):
    inlines = [
        FunctieEisInline,
    ]

class RolForm(ModelForm):
    class Meta:
        model = Rol

    taken = ModelMultipleChoiceField(queryset=Taak.objects.all())

    def __init__(self, *args, **kwargs):
        super(RolForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['taken'].initial = self.instance.taken.all()

    def save(self, *args, **kwargs):
        instance = super(RolForm, self).save(commit=False)
        self.fields['taken'].initial.update(rol=None)
        self.cleaned_data['taken'].update(rol=instance)
        return instance

class RolAdmin(admin.ModelAdmin):
    form = RolForm

class TaakForm(ModelForm):
    class Meta:
        model = Taak

    rollen = ModelMultipleChoiceField(queryset=Rol.objects.all())

    def __init__(self, *args, **kwargs):
        super(TaakForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['rollen'].initial = self.instance.rollen.all()

    def save(self, *args, **kwargs):
        instance = super(TaakForm, self).save(commit=False)
        self.fields['rollen'].initial.update(taak=None)
        self.cleaned_data['rollen'].update(taak=instance)
        return instance

class TaakAdmin(admin.ModelAdmin):
    form = TaakForm

admin.site.register(Afdeling, AfdelingAdmin)
admin.site.register(Taak, TaakAdmin)
admin.site.register(Verantwoordelijkheid)
admin.site.register(Functie, FunctieAdmin)
admin.site.register(Sector)
admin.site.register(FunctieEis)
admin.site.register(Rol, RolAdmin)
admin.site.register(RolGeneriek)
