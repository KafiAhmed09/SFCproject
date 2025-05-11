from django import forms
from .models import Order, Parcel

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['parcel', 'location']

    # You can override the init method to customize the form behavior
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit the available parcels to those that are active or match certain criteria
        self.fields['parcel'].queryset = Parcel.objects.all()
