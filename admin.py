from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *
from django.forms import Textarea, SelectMultiple, ModelForm, ModelMultipleChoiceField

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

admin.site.register(Afdeling, MPTTModelAdmin)
admin.site.register(Taak)
admin.site.register(Verantwoordelijkheid)
admin.site.register(Functie, FunctieAdmin)
admin.site.register(Sector)
admin.site.register(FunctieEis)
