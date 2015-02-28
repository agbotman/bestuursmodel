from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^bestuursmodel/$', bestuursmodel, name='bestuursmodel'),
    url(r'^bestuursmodel/uitgangspunten/$', bestuursmodel_uitgangspunten, name='bestuursmodel_uitgangspunten'),
    url(r'^bestuursmodel/sectoren/$', bestuursmodel_sectoren, name='bestuursmodel_sectoren'),
    url(r'^bestuursmodel/uitwerking/$', bestuursmodel_uitwerking, name = 'bestuursmodel_uitwerking'),
    url(r'^bestuursmodel/planningcontrol/$', bestuursmodel_planningcontrol, name = 'bestuursmodel_planningcontrol'),
    url(r'^bestuursmodel/afdeling/$', afdeling),
    url(r'^bestuursmodel/afdeling/(\w+)/$', afdeling),
    url(r'^bestuursmodel/afdeling/(\w+)/(\w+)/$', afdeling),
    url(r'^bestuursmodel/functie/$', ListFunctieView.as_view(), name='functie_list'),
    url(r'^bestuursmodel/functie/add/$', AddFunctieView.as_view(), name='functie_add'),
    url(r'^bestuursmodel/functie/(?P<pk>\d+)/$', ChangeFunctieView.as_view(), name='functie_change'),
    url(r'^bestuursmodel/functie/(?P<pk>\d+)/delete/$', FunctieDelete.as_view(), name='functie_delete'),
#    url(r'^bestuursmodel/functietype/$', ListFunctietypeView.as_view(), name='functietype_list'),
)
