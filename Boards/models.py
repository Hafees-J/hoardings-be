from django.db import models

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    renewal_at = models.DateField(null=True, blank=True)
    next_renewal_at = models.DateField(null=True, blank=True)
    renewalby = models.CharField(max_length=100, null=True, blank=True)
    createdby = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Board {self.id} - {self.location}"


