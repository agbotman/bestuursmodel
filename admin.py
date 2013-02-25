from django.contrib import admin
from .models import *
from django.forms import Textarea

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

class FunctieInline(admin.TabularInline):
    model = Functie.taken.through

class TaakAdmin(admin.ModelAdmin):
    inlines = [
        FunctieInline,
    ]

admin.site.register(Afdeling, AfdelingAdmin)
admin.site.register(Taak, TaakAdmin)
admin.site.register(Verantwoordelijkheid)
admin.site.register(Functie, FunctieAdmin)
admin.site.register(Sector)
admin.site.register(FunctieEis)
admin.site.register(AfdelingFunctie)
