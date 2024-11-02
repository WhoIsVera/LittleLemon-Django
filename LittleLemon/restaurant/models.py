from django.db import models
from django.utils import timezone
# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} : {str(self.price)}"

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.booking_date}"
