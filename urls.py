from django.conf.urls import include, url
from views import *

beschrijving_patterns = [
    url(r'^uitgangspunten/$', bestuursmodel, name='bestuursmodel_uitgangspunten'),
    url(r'^sectoren/$', bestuursmodel, name='bestuursmodel_sectoren'),
    url(r'^uitwerking/$', bestuursmodel, name = 'bestuursmodel_uitwerking'),
    url(r'^planningcontrol/$', bestuursmodel, name = 'bestuursmodel_planningcontrol'),
]

urlpatterns = [
    url(r'^$', bestuursmodel, name='bestuursmodel_inleiding'),
    url(r'^afdelingen/$', afdelingen, name='afdelingen'),
    url(r'^afdeling/$', afdeling),
    url(r'^afdeling/(\w+)/$', afdeling, name='afdeling'),
    url(r'^afdeling/(\w+)/(\w+)/$', afdeling),
#    url(r'^functie/$', ListFunctieView.as_view(), name='functie_list'),
    url(r'^functies/$', functies, name='functies'),
    url(r'^functie/(\w+)/$', functie, name='functie'),
    url(r'^functie/add/$', AddFunctieView.as_view(), name='functie_add'),
    url(r'^functie/(?P<pk>\d+)/$', ChangeFunctieView.as_view(), name='functie_change'),
    url(r'^functie/(?P<pk>\d+)/delete/$', FunctieDelete.as_view(), name='functie_delete'),
#    url(r'^bestuursmodel/functietype/$', ListFunctietypeView.as_view(), name='functietype_list'),
    url(r'^inleiding/', include(beschrijving_patterns)),
]
