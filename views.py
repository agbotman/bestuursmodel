from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *

def afdelingoverzicht(request):
    return render_to_response('afdelingoverzicht.html')

def afdeling(request, afdelingsnaam):
    afdeling = Afdeling.objects.get(naam=afdelingsnaam)
    afdelingen = Afdeling.objects.all()
    return render_to_response('afdeling.html',
                              {'afdeling': afdeling, 'afdelingen': afdelingen},
                              RequestContext(request))
