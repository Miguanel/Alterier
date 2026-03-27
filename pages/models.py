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