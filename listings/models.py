from django.db import models

import settings

class User(AbstractUser):
    GUEST = 'guest'
    HOST = 'host'
    USER_TYPE_CHOICES = [
        (GUEST, 'Guest'),
        (HOST, 'Host'),
    ]

    user_type = models.CharField(
        max_length=5,
        choices=USER_TYPE_CHOICES,
        default=GUEST,
    )

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    available_from = models.DateField()
    available_until = models.DateField()
    image = models.ImageField(upload_to='properties/')

    def __str__(self):
        return self.title

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('canceled', 'Canceled')], default='pending')

    def __str__(self):
        return f"Booking by {self.guest.username} for {self.property.title}"
    

class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.guest.username} for {self.booking.property.title}"
    

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('completed', 'Completed'), ('pending', 'Pending'), ('failed', 'Failed')], default='pending')

    def __str__(self):
        return f"Payment by {self.guest.username} for {self.booking.property.title}"
