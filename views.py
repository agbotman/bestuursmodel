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

def bestuursmodel(request):
    return render(request, 'bestuursmodel.html',
                             {'afdelingen': Afdeling.objects.all(),}
                  )

def bestuursmodel_uitgangspunten(request):
    return render(request, 'bestuursmodel_uitgangspunten.html',
                             {'afdelingen': Afdeling.objects.all(),}
                  )

def bestuursmodel_sectoren(request):
    return render(request, 'bestuursmodel_sectoren.html',
                             {'afdelingen': Afdeling.objects.all(),}
                  )

def bestuursmodel_uitwerking(request):
    return render(request, 'bestuursmodel_uitwerking.html',
                             {'afdelingen': Afdeling.objects.all(),}
                  )

def bestuursmodel_planningcontrol(request):
    return render(request, 'bestuursmodel_planningcontrol.html',
                             {'afdelingen': Afdeling.objects.all(),}
                  )

def afdeling(request, afdelingsid=1):
    try:
        afdeling = Afdeling.objects.get(id=int(afdelingsid))
    except:
        raise Http404
    return render(request, 'afdeling.html', 
                            {'afdeling': afdeling,
                             'afdelingen': Afdeling.objects.all(),}
                  )


def functie(request, functieid=1):
    try:
        functie = Functie.objects.get(id=int(functieid))
    except:
        raise Http404
    functies = Functie.objects.all()
    return render(request, 'functie.html',
                              {'functie': functie,
                               'functies': functies,
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
        
    