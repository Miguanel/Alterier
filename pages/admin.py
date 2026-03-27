from django.contrib import admin
from .models import ContactMessage, HomePageContent

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read']
    search_fields = ['name', 'email', 'message']

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    # Zabezpieczenie: Można dodać tylko jeden wpis z konfiguracją strony głównej
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True