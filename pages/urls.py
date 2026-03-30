from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('o-mnie/', views.about, name='about'),
    path('kontakt/', views.contact, name='contact'),
]