from django.contrib import admin
from .models import *
from django.forms import Textarea

class AfdelingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }

admin.site.register(Afdeling, AfdelingAdmin)
admin.site.register(Taak)
admin.site.register(Verantwoordelijkheid)
admin.site.register(Functie)
admin.site.register(Sector)
admin.site.register(FunctieEis)
admin.site.register(AfdelingFunctie)
