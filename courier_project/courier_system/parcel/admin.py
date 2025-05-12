from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Merchant, Parcel, Order

admin.site.register(Merchant)
admin.site.register(Parcel)  
admin.site.register(Order)
