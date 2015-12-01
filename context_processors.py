from .models import Afdeling

def afdelingen(request):
    return {'root_afd': Afdeling.objects.filter(level=0)}
