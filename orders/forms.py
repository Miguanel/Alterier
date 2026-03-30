from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dodajemy nasze mistyczne klasy CSS do każdego pola formularza
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full bg-mrok border border-kociolek rounded-full py-3 px-6 text-ksiega focus:outline-none focus:border-kolor-czary transition shadow-sm placeholder-kociolek mb-4'
            })