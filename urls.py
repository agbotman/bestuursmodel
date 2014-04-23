from django.conf.urls import patterns, url, include

urlpatterns = patterns('bestuursmodel.views',
    (r'^bestuursmodel/$', 'afdeling'),
    (r'^bestuursmodel/afdeling/$', 'afdeling'),
    (r'^bestuursmodel/afdeling/(\w+)/$', 'afdeling'),
    (r'^bestuursmodel/afdeling/(\w+)/(\w+)/$', 'afdeling'),
    (r'^bestuursmodel/functie/$', 'functie'),
    (r'^bestuursmodel/functie/(\w+)/$', 'functie'),
    (r'^bestuursmodel/add/functie/?$', 'newFunctie'), 
)
