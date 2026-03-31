from django.contrib import admin
from .models import Service, BookingRequest, TarotSection, ServiceType


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_type', 'price', 'event_date') # Upewnij się, że nazwa to service_type
    list_filter = ('service_type', 'event_date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'service', 'requested_date', 'is_resolved', 'created_at']
    list_filter = ['is_resolved', 'service']

@admin.register(TarotSection)
class TarotSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}