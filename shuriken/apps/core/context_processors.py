# core/context_processors.py
from django.conf import settings

def core(request):
    kwargs = {
        'SHURIKEN_DEV_FEATURES': settings.SHURIKEN_DEV_FEATURES,
        'SHURIKEN_VERSION': settings.SHURIKEN_VERSION
    }
    return kwargs