from .models import Category

def menu_categories(request):
    """Pobiera wszystkie kategorie z bazy i przekazuje je do base.html"""
    return {
        'all_categories': Category.objects.all()
    }