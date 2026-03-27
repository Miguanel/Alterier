from django.contrib import admin
from .models import Service, BookingRequest

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'service_type', 'price', 'duration_minutes', 'is_active']
    list_filter = ['service_type', 'is_active']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'service', 'requested_date', 'is_resolved', 'created_at']
    list_filter = ['is_resolved', 'service']