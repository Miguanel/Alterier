from django.shortcuts import render
from shop.models import Product


def home(request):
    # Pobieramy 4 najnowsze i dostępne produkty do sekcji "Wyróżnione"
    featured_products = Product.objects.filter(available=True)[:4]

    return render(request, 'pages/home.html', {'featured_products': featured_products})