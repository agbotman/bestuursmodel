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
    activelink = "bestuursmodel"
    if request.path == "/bestuursmodel/":
        detail = 'inleiding'
    else:
        detail = request.path.split('/')[-2]
    detail_html = 'bestuursmodel_' + detail + '.html'
    if detail == 'planningcontrol':
        title = 'Planning & Control'
    else:
        title = detail.title()
    return render(request, 'bestuursmodel.html',
                             {'activelink': activelink,
                              'sublink': detail,
                              'detail_html': detail_html,
                              'title': title,
							   }
                  )

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

class FunctieUpdate(UpdateView):
    model = Functie
    fields = ['naam', 'beschrijving', 'afdeling', 'functietype', 'functietaken']
    
class FunctieDelete(DeleteView):
    model = Functie
    success_url = reverse_lazy('functie_list')
    
class AddFunctieView(CreateView):
    form_class = FunctieForm
    template_name = 'bestuursmodel/functie_form.html'
    success_url = reverse_lazy('functie_list')
    
    def get_context_data(self, **kwargs):
        context = super(AddFunctieView, self).get_context_data(**kwargs)
        context['functies'] = Functie.objects.all()
        return context

    
class ChangeFunctieView(UpdateView):
    form_class = FunctieForm
    model = Functie
    success_url = reverse_lazy('functie_list')
    
    def get_context_data(self, **kwargs):
        context = super(ChangeFunctieView, self).get_context_data(**kwargs)
        context['functies'] = Functie.objects.all()
        return context

class ListFunctieView(ListView):
    template_name = 'functie.html'
    queryset = Functie.objects.order_by('afdeling')
        
    