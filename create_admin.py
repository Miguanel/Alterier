import os
import django

# Ustawienie środowiska Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Dane Twojego admina - możesz je zmienić tutaj
USERNAME = 'admin_angie'
EMAIL = 'admin@example.com'
PASSWORD = 'cieslak!' # Zmień na bezpieczne!

if not User.objects.filter(username=USERNAME).exists():
    print(f'Tworzenie superużytkownika {USERNAME}...')
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print('Superużytkownik stworzony pomyślnie.')
else:
    print(f'Użytkownik {USERNAME} już istnieje.')