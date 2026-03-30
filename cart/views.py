from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart


@require_POST
def cart_add(request, product_id):
    """Widok dodający produkt do koszyka (wymaga metody POST)."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # Dodajemy 1 sztukę produktu
    cart.add(product=product, quantity=1, override_quantity=False)

    # Po dodaniu od razu przenosimy klienta do koszyka
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """Widok usuwający produkt z koszyka."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect('cart:cart_detail')


def cart_detail(request):
    """Widok wyświetlający całą zawartość koszyka."""
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})