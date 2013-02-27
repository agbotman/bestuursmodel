from django.conf.urls import patterns, url, include

urlpatterns = patterns('bestuursmodel.views',
    (r'^bestuursmodel/$', 'afdelingoverzicht'),
    (r'^bestuursmodel/afdeling/$', 'afdeling'),
    (r'^bestuursmodel/afdeling/(\w+)/$', 'afdeling'),
)
