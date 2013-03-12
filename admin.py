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

# class TaakInline(admin.TabularInline):
#     model = Taak

# class RolAdmin(admin.ModelAdmin):
#     inlines = [
#         TaakInline,
#    ]


class RolForm(ModelForm):
    class Meta:
        model = Rol

    taken = ModelMultipleChoiceField(queryset=Taak.objects.all())

    def __init__(self, *args, **kwargs):
        super(RolForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['taken'].initial = self.instance.taken.all()

    def save(self, *args, **kwargs):
        # FIXME: 'commit' argument is not handled
        # TODO: Wrap reassignments into transaction
        # NOTE: Previously assigned Foos are silently reset
        instance = super(RolForm, self).save(commit=False)
        self.fields['taken'].initial.update(rol=None)
        self.cleaned_data['taken'].update(rol=instance)
        return instance

class RolAdmin(admin.ModelAdmin):
    form = RolForm

admin.site.register(Afdeling, AfdelingAdmin)
admin.site.register(Taak)
admin.site.register(Verantwoordelijkheid)
admin.site.register(Functie, FunctieAdmin)
admin.site.register(Sector)
admin.site.register(FunctieEis)
admin.site.register(Rol, RolAdmin)
admin.site.register(RolGeneriek)
