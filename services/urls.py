from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),
    # NOWA ŚCIEŻKA DO KATEGORII USŁUG:
    path('kategoria/<slug:type_slug>/', views.service_list, name='service_list_by_type'),
    path('<slug:slug>/', views.service_detail, name='service_detail'),
]