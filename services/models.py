from django.urls import reverse
from django.db import models


class ServiceType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa typu (np. Czytanie Tarota)")
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Typ usługi"
        verbose_name_plural = "Typy usług"

    def __str__(self):
        return self.name


class Service(models.Model):
    # Opcje wyboru typu usługi dla klientki w panelu


    title = models.CharField(max_length=200, verbose_name="Nazwa usługi")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL (Slug)")
    service_type = models.ForeignKey(ServiceType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Typ usługi")
    description = models.TextField(verbose_name="Opis usługi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena")
    duration_minutes = models.PositiveIntegerField(verbose_name="Czas trwania (minuty)",
                                                   help_text="Np. 60 dla godzinnej sesji")
    event_date = models.DateTimeField(blank=True, null=True,
                                      verbose_name="Data i czas wydarzenia (zostaw puste dla usług ciągłych)")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="Zdjęcie poglądowe")
    is_active = models.BooleanField(default=True, verbose_name="Aktywna (wyświetlaj na stronie)")

    def get_absolute_url(self):
        # Ta funkcja mówi Django: "zbuduj link do widoku service_detail i przekaż mu mój slug"
        return reverse('services:service_detail', args=[self.slug])
    class Meta:
        verbose_name = "Usługa"
        verbose_name_plural = "Usługi"

    def __str__(self):
        return self.title


class BookingRequest(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='requests',
                                verbose_name="Dotyczy usługi")
    client_name = models.CharField(max_length=100, verbose_name="Imię klienta")
    client_email = models.EmailField(verbose_name="E-mail klienta")
    message = models.TextField(blank=True, verbose_name="Wiadomość / Oczekiwania (np. temat do tarota)")

    # Kiedy klient chce się spotkać
    requested_date = models.DateTimeField(null=True, blank=True, verbose_name="Proponowany termin")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data wysłania zapytania")
    is_resolved = models.BooleanField(default=False, verbose_name="Obsłużone (odznacz, gdy odpiszesz)")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Zapytanie o rezerwację"
        verbose_name_plural = "Zapytania o rezerwacje"

    def __str__(self):
        return f"Zapytanie od {self.client_name} - {self.service.title}"

class TarotSection(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł sekcji (np. Zwierciadło Twojej Duszy)")
    description = models.TextField(verbose_name="Treść opisu")
    image = models.ImageField(upload_to='tarot_sections/', verbose_name="Zdjęcie")
    order = models.PositiveIntegerField(default=0, verbose_name="Kolejność wyświetlania (1, 2, 3...)")

    class Meta:
        ordering = ['order']
        verbose_name = "Sekcja Opisowa Tarota"
        verbose_name_plural = "Sekcje Opisowe Tarota"

    def __str__(self):
        return self.title