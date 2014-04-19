from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *
from django.forms import Textarea, SelectMultiple, ModelForm, ModelMultipleChoiceField

#class AfdelingAdmin(admin.ModelAdmin):
#    formfield_overrides = {
#        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
#    }

class RolInline(admin.TabularInline):
    model = Rol
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }

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
        RolInline
    ]
    
#class RolInline(admin.TabularInline):
#    model = Rol.taken.through

#class TaakAdmin(admin.ModelAdmin):
#    inlines = [
#        RolInline,
#    ]
    
class TaakInline(admin.TabularInline):
    model = Taak.rollen.through

class RolAdmin(admin.ModelAdmin):
    inlines = [
        TaakInline,
    ]
    

#class RolForm(ModelForm):
#    class Meta:
#        model = Rol

#    taken = ModelMultipleChoiceField(queryset=Taak.objects.all())

#    def __init__(self, *args, **kwargs):
#        super(RolForm, self).__init__(*args, **kwargs)
#        if self.instance:
#            self.fields['taken'].initial = self.instance.taken.all()

#    def save(self, *args, **kwargs):
#        instance = super(RolForm, self).save(commit=False)
#        self.fields['taken'].initial.update(rol=None)
#        self.cleaned_data['taken'].update(rol=instance)
#        return instance

#class RolAdmin(admin.ModelAdmin):
#    form = RolForm


admin.site.register(Afdeling, MPTTModelAdmin)
admin.site.register(Taak)
admin.site.register(Verantwoordelijkheid)
admin.site.register(Functie, FunctieAdmin)
admin.site.register(Sector)
admin.site.register(FunctieEis)
admin.site.register(Rol, RolAdmin)
admin.site.register(RolGeneriek)
