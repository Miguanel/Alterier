from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'shop/product_list.html', context)


# NOWA FUNKCJA: Detale produktu
def product_detail(request, slug):
    # Szuka produktu po slugu, a jeśli nie znajdzie, wyrzuca błąd 404
    product = get_object_or_404(Product, slug=slug, available=True)

    context = {'product': product}
    return render(request, 'shop/product_detail.html', context)