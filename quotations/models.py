from django.db import models
from packages.models import Packages

# Create your models here.


class Quotation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    remarks = models.TextField()
    date = models.DateTimeField()
    packNo = models.ForeignKey(Packages, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
