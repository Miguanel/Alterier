from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    # Pobieramy wszystkie dostępne produkty
    products = Product.objects.filter(available=True)

    # Jeśli w adresie URL przekazano "category_slug" (np. "naklejki")
    if category_slug:
        # Szukamy tej kategorii w bazie danych (jeśli nie ma, wywali błąd 404)
        category = get_object_or_404(Category, slug=category_slug)
        # Filtrujemy produkty, żeby pokazać tylko te z danej kategorii
        products = products.filter(category=category)

    return render(request, 'shop/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


# NOWA FUNKCJA: Detale produktu
def product_detail(request, slug):
    # Szuka produktu po slugu, a jeśli nie znajdzie, wyrzuca błąd 404
    product = get_object_or_404(Product, slug=slug, available=True)

    context = {'product': product}
    return render(request, 'shop/product_detail.html', context)