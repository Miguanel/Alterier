from .cart import Cart

def cart(request):
    """Dzięki temu słownik 'cart' będzie dostępny w każdym szablonie HTML na stronie."""
    return {'cart': Cart(request)}