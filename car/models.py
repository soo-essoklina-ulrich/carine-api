from django.db import models

from authentication.models import CustomerUser


# Create your models here.


class Car(models.Model):
    model = models.CharField(max_length=100)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_by = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)


class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)