from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *
from django.forms import Textarea, SelectMultiple, ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.admin import SimpleListFilter

class FunctieEisInline(admin.TabularInline):
    model = FunctieEis.functies.through
    extra = 1
    verbose_name = "Functie eis"
    verbose_name_plural = "Eisen voor deze functie"

class FunctieTaakInline(admin.TabularInline):
    model = Functie.taken.through
    extra = 1
    verbose_name_plural = "Taken voor deze functie"
    
class FunctieAfdelingenInline(admin.TabularInline):
    model = Afdeling_Functie
    extra = 1
    verbose_name_plural = "Afdelingen voor deze functie"
    
class FunctieAdmin(admin.ModelAdmin):
    model = Functie
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }
    inlines = [
        FunctieTaakInline,
        FunctieAfdelingenInline,
        FunctieEisInline,
    ]
    
    list_display = ('naam', 'functietype')
    list_editable = ('functietype',)
    list_filter = ()
    
    class Media:
        # to omit header above all inline records
        css = { "all" : ("css/bestuursmodel/hide_admin_original.css",
        # and to make width of change list filter 200px
                         "css/bestuursmodel/change_list_filter_right_200.css",) }
        js = { "all" : ("js/list_filter_collapse.js",) }
               
class AfdelingAdminForm(ModelForm):
    class Meta:
        model = Afdeling
        fields = ('nummer', 'naam', 'taakbeschrijving', 'rapporteert_aan',
                    'sector', 'permanent', 'startdatum', 'einddatum',)
        
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
            afdeling.save()

        return afdeling

class AfdelingAdmin(MPTTModelAdmin):
    form = AfdelingAdminForm
    
class FunctieTaakAdmin(admin.ModelAdmin):
    list_display = ('naam', 'functietype')
    list_editable = ('functietype',)


admin.site.register(Afdeling, AfdelingAdmin)
admin.site.register(Taak)
admin.site.register(Verantwoordelijkheid)
admin.site.register(Functie, FunctieAdmin)
admin.site.register(FunctieTaak, FunctieTaakAdmin)
admin.site.register(FunctieType)
admin.site.register(Sector)
admin.site.register(FunctieEis)
