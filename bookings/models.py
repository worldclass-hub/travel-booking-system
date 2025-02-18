from django.conf import settings  # Import settings
from django.db import models
from tours.models import Tour

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use the custom user model
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    guests = models.PositiveIntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tour.title} on {self.date}"
