from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="tour_images/")
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.title
