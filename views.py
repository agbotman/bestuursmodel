from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.html import escape
from django.http import HttpResponseRedirect

def addInstance(request, addForm, field):
    redirect_to = request.REQUEST.get('next', '')
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            try:
                newObject = form.save()
            except forms.ValidationError, error:
                newObject = None
            if newObject:
                return HttpResponseRedirect(redirect_to)
    else:
        form = addForm()
    pageContext = {'form': form, 'field': field, 'redirect_to': redirect_to,}
    return render_to_response("add_instance.html", pageContext, RequestContext(request))


def afdeling(request, afdelingsid=1):
    try:
        afdeling = Afdeling.objects.get(id=int(afdelingsid))
    except:
        afdeling = Afdeling.objects.get(id=1)
    hoofdbestuur = Afdeling.objects.get(id=1)
    return render_to_response('afdeling.html',
                              {'afdeling': afdeling,
                               'afdelingen': Afdeling.objects.all(),},
                              RequestContext(request))

def functie(request, functieid=1):
    try:
        functie = Functie.objects.get(id=int(functieid))
    except:
        functie = Functie.objects.get(id=1)
    functies = Functie.objects.all()
    return render_to_response('functie.html',
                              {'functie': functie,
                               'functies': functies,
                               },
                              RequestContext(request))


@login_required
def newFunctie(request):
    return addInstance(request, FunctieForm, 'functie')


