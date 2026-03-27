from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # Główny adres strony (np. localhost:8000/)
    path('', views.home, name='home'),
]