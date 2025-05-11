from django.db import models

# Create your models here.
from django.db import models

# Merchant Model
class Merchant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Parcel Model
class Parcel(models.Model):
    PARCEL_TYPES = [
        ('Fragile', 'Fragile'),
        ('Liquid', 'Liquid')
    ]
    weight = models.FloatField()  # Weight of the parcel in kg
    product_type = models.CharField(max_length=10, choices=PARCEL_TYPES)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    invoice_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Parcel from {self.merchant.name} - {self.product_type}"


# Order Model
class Order(models.Model):
    ORDER_LOCATIONS = [
        ('Inside Dhaka', 'Inside Dhaka'),
        ('Division of Dhaka', 'Division of Dhaka'),
        ('Outside Dhaka', 'Outside Dhaka')
    ]
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=ORDER_LOCATIONS)
    cod_charge = models.FloatField(default=0)
    return_charge = models.FloatField(default=0)
    total_charge = models.FloatField()

    def calculate_charge(self):
        # Logic for dynamic charge calculation
        if self.location == 'Inside Dhaka':
            if 0.5 <= self.parcel.weight <= 2:
                self.total_charge = 60
            elif self.parcel.weight == 3:
                self.total_charge = 70
            elif self.parcel.weight == 4:
                self.total_charge = 80
            elif self.parcel.weight == 5:
                self.total_charge = 90
        elif self.location == 'Division of Dhaka':
            if 0.5 <= self.parcel.weight <= 2:
                self.total_charge = 110
            elif self.parcel.weight == 3:
                self.total_charge = 130
            elif self.parcel.weight == 4:
                self.total_charge = 150
            elif self.parcel.weight == 5:
                self.total_charge = 170
            self.cod_charge = self.total_charge * 0.01
            self.return_charge = self.total_charge * 0.5
        elif self.location == 'Outside Dhaka':
            if 0.5 <= self.parcel.weight <= 2:
                self.total_charge = 130
            elif self.parcel.weight == 3:
                self.total_charge = 150
            elif self.parcel.weight == 4:
                self.total_charge = 170
            elif self.parcel.weight == 5:
                self.total_charge = 190
            self.cod_charge = self.total_charge * 0.01
            self.return_charge = self.total_charge * 0.5
        
        # Update the total charge after COD and return charge calculation
        self.total_charge += self.cod_charge + self.return_charge
        self.save()

    def __str__(self):
        return f"Order for {self.parcel} to {self.location} - Total: {self.total_charge}"
