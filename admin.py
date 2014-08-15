from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *
from django.forms import Textarea, SelectMultiple, ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple

class FunctieEisInline(admin.TabularInline):
    model = FunctieEis.functies.through
    extra = 1
    verbose_name = "Functie eis"
    verbose_name_plural = "Functie eisen voor deze functie"

class FunctieAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }
    inlines = [
        FunctieEisInline,
    ]

       
class AfdelingAdminForm(ModelForm):
    class Meta:
        model = Afdeling
        
    taken = ModelMultipleChoiceField(
        queryset=Taak.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Taken',
            is_stacked=False
        )
    )

    bevoegdheden = ModelMultipleChoiceField(
        queryset=Bevoegdheid.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Bevoegdheden',
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(AfdelingAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['taken'].initial = self.instance.taken.all()
            self.fields['bevoegdheden'].initial = self.instance.bevoegdheden.all()

    def save(self, commit=True):
        afdeling = super(AfdelingAdminForm, self).save(commit=False)  
        if commit:
            afdeling.save()

        if afdeling.pk:
            afdeling.taken = self.cleaned_data['taken']
            afdeling.bevoegdheden = self.cleaned_data['bevoegdheden']
#            self.save()
            afdeling.save()

        return afdeling

class AfdelingAdmin(MPTTModelAdmin):
    form = AfdelingAdminForm

 

admin.site.register(Afdeling, AfdelingAdmin)
admin.site.register(Taak)
admin.site.register(Verantwoordelijkheid)
admin.site.register(Functie, FunctieAdmin)
admin.site.register(Sector)
admin.site.register(FunctieEis)
