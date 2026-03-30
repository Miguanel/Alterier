from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Lista wszystkich produktów
    path('', views.product_list, name='product_list'),

    # LISTA PRODUKTÓW Z KONKRETNEJ KATEGORII (To tej ścieżki brakowało lub miała inną nazwę!)
    path('kategoria/<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    # Szczegóły konkretnego produktu
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]