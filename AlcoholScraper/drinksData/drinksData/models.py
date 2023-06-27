from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Drink(models.Model):
    name = models.CharField(max_length=100)
    units = models.IntegerField()
    volume = models.IntegerField()
    content = models.DecimalField(decimal_places=4, max_digits=7, 
                                  validators=[MaxValueValidator(1), MinValueValidator(0)])
    price = models.DecimalField(decimal_places=2, max_digits=6)
    sale_price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)
    link = models.CharField()
    type = models.CharField()
    tvolume = models.IntegerField()
    talc = models.DecimalField(decimal_places=4, max_digits=8)
    alc_per_dol = models.DecimalField(decimal_places=4, max_digits=7)
    store=models.CharField()


    def __str__(self) -> str:
        return self.name
    

