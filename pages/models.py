from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Imię")
    email = models.EmailField(verbose_name="Adres e-mail")
    subject = models.CharField(max_length=200, verbose_name="Temat", blank=True)
    message = models.TextField(verbose_name="Treść wiadomości")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data wysłania")
    is_read = models.BooleanField(default=False, verbose_name="Przeczytane")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Wiadomość z formularza"
        verbose_name_plural = "Wiadomości z formularza"

    def __str__(self):
        return f"Wiadomość od {self.name} ({self.email})"

class HomePageContent(models.Model):
    # SEKCJA: KOLEKCJE (Zielona)
    collections_title = models.CharField(max_length=200, default="Odkryj więcej sztuki, magii i wiedzy.", verbose_name="Tytuł (Sekcja Kolekcje)")
    collections_text = models.TextField(default="Znajdziesz tu wszystko – od ilustracji, przez plany lekcji norweskiego, aż po sesje Tarota.", verbose_name="Tekst (Sekcja Kolekcje)")
    collections_btn_text = models.CharField(max_length=100, default="Przeglądaj sklep", verbose_name="Tekst na przycisku")
    collections_image = models.ImageField(upload_to='homepage/', blank=True, null=True, verbose_name="Zdjęcie poglądowe (Sekcja Kolekcje)")

    # SEKCJA: O MNIE (Niebieska)
    about_title = models.CharField(max_length=200, default="Cześć!", verbose_name="Tytuł (Sekcja O mnie)")
    about_text = models.TextField(default="Tworzę sztukę, magiczne i lingwistyczne materiały oraz pomagam w odkrywaniu siebie poprzez numerologię i Tarota. Chcę dzielić się z Wami moim światem.", verbose_name="Tekst (Sekcja O mnie)")
    about_btn_text = models.CharField(max_length=100, default="Poznaj moją historię", verbose_name="Tekst na przycisku")
    about_image = models.ImageField(upload_to='homepage/', blank=True, null=True, verbose_name="Zdjęcie / Portret (Sekcja O mnie)")

    class Meta:
        verbose_name = "Treść Strony Głównej"
        verbose_name_plural = "Treść Strony Głównej"

    def __str__(self):
        return "Ustawienia tekstów i zdjęć na stronie głównej"