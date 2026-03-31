from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, BookingRequest, TarotSection, ServiceType
from django.contrib import messages
from django.utils import timezone


def service_list(request, type_slug=None):
    now = timezone.now()

    # Pobieramy wszystkie usługi
    upcoming_services = Service.objects.filter(event_date__gte=now) | Service.objects.filter(event_date__isnull=True)
    past_services = Service.objects.filter(event_date__lt=now).order_by('-event_date')

    # Jeśli kliknięto w konkretną kategorię w menu, filtrujemy wyniki!
    service_type = None
    if type_slug:
        service_type = get_object_or_404(ServiceType, slug=type_slug)
        upcoming_services = upcoming_services.filter(service_type=service_type)
        past_services = past_services.filter(service_type=service_type)

    tarot_sections = TarotSection.objects.all()

    return render(request, 'services/service_list.html', {
        'service_type': service_type,
        'upcoming_services': upcoming_services,
        'past_services': past_services,
        'tarot_sections': tarot_sections,
    })

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)

    # Obsługa formularza rezerwacji
    if request.method == 'POST':
        client_name = request.POST.get('name')
        client_email = request.POST.get('email')
        message = request.POST.get('message')

        # Zapisujemy zapytanie do bazy danych
        BookingRequest.objects.create(
            service=service,
            client_name=client_name,
            client_email=client_email,
            message=message
        )
        # Przekierowujemy z powrotem na listę z prostym parametrem sukcesu (możemy to potem rozbudować)
        return redirect('services:service_list')

    return render(request, 'services/service_detail.html', {'service': service})