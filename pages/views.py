from django.shortcuts import render
from shop.models import Product
from .models import HomePageContent  # Importujemy nasz nowy model



def home(request):
    featured_products = Product.objects.filter(available=True)[:4]

    # Pobieramy pierwszy i jedyny wpis z ustawieniami.
    # Jeśli klientka jeszcze go nie dodała w panelu, zmienna będzie pusta.
    content = HomePageContent.objects.first()

    return render(request, 'pages/home.html', {
        'featured_products': featured_products,
        'content': content,
    })

def about(request):
    """Widok strony O mnie"""
    return render(request, 'pages/about.html')

def contact(request):
    """Widok strony Kontakt"""
    return render(request, 'pages/contact.html')