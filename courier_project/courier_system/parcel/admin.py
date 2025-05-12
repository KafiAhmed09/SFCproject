from django.contrib import admin


from django.contrib import admin
from .models import Merchant, Parcel, Order

admin.site.register(Merchant)
admin.site.register(Parcel)  
admin.site.register(Order)
