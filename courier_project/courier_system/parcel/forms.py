from django import forms
from .models import Order, Parcel

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['parcel', 'location']

   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parcel'].queryset = Parcel.objects.all()
