from django.conf.urls import patterns, url, include

urlpatterns = patterns('bestuursmodel.views',
    (r'^bestuursmodel/$', 'afdelingoverzicht'),
    (r'^bestuursmodel/afdeling/$', 'afdelingoverzicht'),
    (r'^bestuursmodel/afdeling/(\w+)/$', 'afdeling'),
)
