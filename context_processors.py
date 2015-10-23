from .models import Afdeling

def afdelingen(request):
    hoofdbestuur = Afdeling.objects.get(naam='Hoofdbestuur')
    alv = Afdeling.objects.get(naam='Algemene vergadering')
    return {'alv_afdelingen': alv.get_descendants(include_self=True),
            'hb_afdelingen': hoofdbestuur.get_descendants(include_self=True),
            'alv': alv,
            'hb': hoofdbestuur,
           } 