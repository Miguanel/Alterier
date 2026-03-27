from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nazwa kategorii")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL (Slug)")

    class Meta:
        ordering = ['name']
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.name


class Product(models.Model):
    # Relacja do kategorii
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="Kategoria")

    name = models.CharField(max_length=200, verbose_name="Nazwa produktu")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL (Slug)")
    description = models.TextField(verbose_name="Opis")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena")

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Zdjęcie produktu")

    # Flagi dla produktów cyfrowych
    is_digital = models.BooleanField(default=False, verbose_name="Produkt cyfrowy (nie wymaga wysyłki)")
    digital_file = models.FileField(upload_to='digital_products/', blank=True, null=True,
                                    verbose_name="Plik do pobrania (np. PDF)")

    available = models.BooleanField(default=True, verbose_name="Dostępny w sprzedaży")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ostatnia aktualizacja")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __str__(self):
        return self.name