from django.contrib import admin
from .models import Order, OrderItem
from .models import OrderSettings # Upewnij się, że zaimportowałeś OrderSettings na górze pliku!


# To pozwala widzieć przedmioty bezpośrednio wewnątrz zamówienia w panelu
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]



@admin.register(OrderSettings)
class OrderSettingsAdmin(admin.ModelAdmin):
    # Wyłączamy możliwość dodawania wielu konfiguracji (przycisk "Dodaj" zniknie, jeśli jedna już istnieje)
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True