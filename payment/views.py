from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from orders.models import Order
from orders.models import Order, OrderSettings


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # 1. Symulacja opłacenia
        order.paid = True
        order.save()

        # 2. Pobieramy ustawienia E-mail z bazy danych
        settings = OrderSettings.objects.first()

        # Jeśli ustawienia istnieją w bazie, używamy ich (podmieniając tagi na dane)
        if settings:
            sender = settings.sender_email
            subject = settings.email_subject.format(order_id=order.id)
            message = settings.email_message.format(
                order_id=order.id,
                first_name=order.first_name
            )
        else:
            # Awaryjny tekst, jeśli nikt jeszcze nie zapisał ustawień w panelu
            sender = 'kontakt@twojeatelier.pl'
            subject = f'Twoje Atelier - Potwierdzenie zamówienia nr {order.id}'
            message = f'Witaj {order.first_name},\n\nTwoje zamówienie nr {order.id} zostało opłacone.'

        # 3. Wysyłanie e-maila
        send_mail(
            subject,
            message,
            sender,
            [order.email],
            fail_silently=False,
        )

        # 4. Przekierowanie do ekranu sukcesu
        return redirect('payment:completed')

    return render(request, 'payment/process.html', {'order': order})


def payment_completed(request):
    # Pobieramy zamówienie, żeby móc wylistować kupione rzeczy na ekranie sukcesu
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    # Oczyszczamy sesję z ID zamówienia (zakupy zakończone)
    if 'order_id' in request.session:
        del request.session['order_id']

    return render(request, 'payment/completed.html', {'order': order})


def payment_canceled(request):
    return render(request, 'payment/canceled.html')