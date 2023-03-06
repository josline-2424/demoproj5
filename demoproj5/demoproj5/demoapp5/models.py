from django.db import models


# Create your models here.
class Store(models.Model):
    prodname = models.CharField(max_length=250)
    prodquantity = models.IntegerField()

    def __str__(self):
        return self.prodname
