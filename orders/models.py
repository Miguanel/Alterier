from django.db import models
from shop.models import Product


class Order(models.Model):
    # DANE KLIENTA
    first_name = models.CharField(max_length=50, verbose_name="Imię")
    last_name = models.CharField(max_length=50, verbose_name="Nazwisko")
    email = models.EmailField(verbose_name="E-mail (do wysyłki PDF)")

    # ADRES (Opcjonalny, bo PDFy nie wymagają adresu)
    address = models.CharField(max_length=250, blank=True, verbose_name="Ulica i nr domu")
    postal_code = models.CharField(max_length=20, blank=True, verbose_name="Kod pocztowy")
    city = models.CharField(max_length=100, blank=True, verbose_name="Miasto")

    # STATUS ZAMÓWIENIA
    created = models.DateTimeField(auto_now_add=True, verbose_name="Utworzono")
    updated = models.DateTimeField(auto_now=True, verbose_name="Zaktualizowano")
    paid = models.BooleanField(default=False, verbose_name="Opłacone")

    # ID ze Stripe (przyda się później do zwrotów)
    stripe_id = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Zamówienie"
        verbose_name_plural = "Zamówienia"

    def __str__(self):
        return f'Zamówienie {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Ilość")

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

class OrderSettings(models.Model):
    sender_email = models.EmailField(
        default='kontakt@twojeatelier.pl',
        verbose_name="E-mail nadawcy"
    )
    email_subject = models.CharField(
        max_length=200,
        default='Twoje Atelier - Potwierdzenie zamówienia nr {order_id}',
        verbose_name="Temat e-maila"
    )
    email_message = models.TextField(
        default='Witaj {first_name},\n\nDziękujemy za zakupy w Atelier!\nTwoje zamówienie nr {order_id} zostało pomyślnie opłacone.\n\nJeśli kupiłaś pliki cyfrowe, możesz je pobrać bezpośrednio ze strony potwierdzenia.\n\nNiech magia będzie z Tobą!',
        verbose_name="Treść e-maila",
        help_text="Możesz użyć tagów: {order_id} oraz {first_name}, system automatycznie podmieni je na dane z zamówienia."
    )

    class Meta:
        verbose_name = "Ustawienia E-mail"
        verbose_name_plural = "Ustawienia E-mail"

    def __str__(self):
        return "Konfiguracja wiadomości po zakupie"

    def save(self, *args, **kwargs):
        # Ta sztuczka sprawia, że w bazie może być tylko jeden taki wpis (ID=1)
        self.pk = 1
        super(OrderSettings, self).save(*args, **kwargs)