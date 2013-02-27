from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *

def afdeling(request, afdelingsid=1):
    try:
        afdeling = Afdeling.objects.get(id=int(afdelingsid))
    except:
        afdeling = Afdeling.objects.get(id=1)
    afdelingen = Afdeling.objects.all()
    return render_to_response('afdeling.html',
                              {'afdeling': afdeling, 'afdelingen': afdelingen},
                              RequestContext(request))

def functie(request, functieid=1):
    try:
        functie = Functie.objects.get(id=int(functieid))
    except:
        functie = Functie.objects.get(id=1)
    functies = Functie.objects.all()
    afdelingfuncties = AfdelingFunctie.objects.filter(functie=functie)
    return render_to_response('functie.html',
                              {'functie': functie,
                               'functies': functies,
                               'afdelingfuncties': afdelingfuncties},
                              RequestContext(request))
