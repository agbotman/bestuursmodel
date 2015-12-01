from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django import forms
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum

def bestuursmodel(request):
    if request.path == "/bestuursmodel/":
        detail = 'inleiding'
    else:
        detail = request.path.split('/')[-2]
    detail_html = 'bestuursmodel_' + detail + '.html'
    if detail == 'planningcontrol':
        title = 'Planning & Control'
    else:
        title = detail.title()  # title case
    context = {'detail_html': detail_html,
               'title': title,
              }
    if detail == 'sectoren':
        context['sectoren'] = Sector.objects.all()
    return render(request, 'bestuursmodel.html', context)

def afdelingen(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        afdelingen = Afdeling.objects.filter(naam__icontains=q)
    else:
        afdelingen = []
        q = ''
    return render(request, 'afdelingen.html',
        {'afdelingen': afdelingen, 'query': q})

def afdeling(request, afdelingsid=1):
    try:
        afdeling = Afdeling.objects.get(id=int(afdelingsid))
    except:
        raise Http404
    return render(request, 'afdeling.html', 
                            {'afdeling': afdeling,}
                  )


def functies(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        functies = Functie.objects.filter(naam__icontains=q)
    else:
        functies = []
        q = ''
    return render(request, 'functies.html',
        {'functies': functies, 'query': q})

def functie(request, functieid=1):
    try:
        functie = Functie.objects.get(id=int(functieid))
    except:
        raise Http404
    return render(request, 'functie.html',
                              {'functie': functie,
                               'uurtotaal': functie.functietaakdetails.aggregate(Sum('uur_per_maand')),
                               }
                  )
