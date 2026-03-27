from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, BookingRequest
from django.contrib import messages


def service_list(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'services/service_list.html', {'services': services})


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