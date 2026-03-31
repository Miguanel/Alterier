from django.db import models
from django.urls import reverse

class Category(models.Model):
    # Pole pozwalające przypiąć kategorię do innej kategorii (tworzenie podzbiorów)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Kategoria nadrzędna")
    name = models.CharField(max_length=200, verbose_name="Nazwa kategorii")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL (Slug)")
    # Pole na unikalny opis podkategorii
    description = models.TextField(blank=True, verbose_name="Opis widoczny na stronie")

    class Meta:
        ordering = ['name']
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        # W panelu admina będzie widać ładną ścieżkę np. "Naklejki -> Zwierzęta"
        if self.parent:
            return f"{self.parent.name} -> {self.name}"
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    # Relacja do kategorii
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="Kategoria")

    # Podstawowe informacje
    name = models.CharField(max_length=200, verbose_name="Nazwa produktu")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL (Slug)")
    description = models.TextField(verbose_name="Opis")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Zdjęcie produktu")

    # Flagi i pliki dla produktów cyfrowych
    is_digital = models.BooleanField(default=False, verbose_name="Produkt cyfrowy (nie wymaga wysyłki)")
    file = models.FileField(upload_to='products/files/', blank=True, null=True, verbose_name="Plik cyfrowy (np. PDF)")

    # Status i daty
    available = models.BooleanField(default=True, verbose_name="Dostępny w sprzedaży")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ostatnia aktualizacja")

    class Meta:
        ordering = ['name']
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])