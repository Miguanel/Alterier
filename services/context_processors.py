from .models import ServiceType

def menu_service_types(request):
    """Pobiera wszystkie typy usług z bazy i przekazuje je do base.html"""
    return {
        'all_service_types': ServiceType.objects.all()
    }